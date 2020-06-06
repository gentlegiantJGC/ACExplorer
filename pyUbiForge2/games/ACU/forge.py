from typing import Tuple, Dict, Optional, List
import logging
import struct
import numpy
from io import BytesIO

from pyUbiForge2.api import BaseForge
from pyUbiForge2.api.data_types import (
    DataFileMetadata,
    DataFileByteLocations,
    DataFileIdentifier,
    FileIdentifier,
    FileResourceType,
    FileName,
)
from pyUbiForge2.util.compression import decompress

CompressionMarker = b'\x33\xAA\xFB\x57\x99\xFA\x04\x10'


class ACUForge(BaseForge):
    GameIdentifier = "ACU"
    NonContainerDataFiles = {16, 145}

    def _parse_forge(self) -> Tuple[
        DataFileMetadata,
        DataFileByteLocations
    ]:
        logging.info(f'Building file tree for {self.forge_name}')

        with open(self.path, 'rb') as forge_file:
            # header
            if forge_file.read(8) != b'scimitar':
                return {}, {}
            forge_file.seek(1, 1)
            forge_file_version, file_data_header_offset = struct.unpack('<iQ', forge_file.read(12))
            if forge_file_version != 27:
                raise Exception(f'Unsupported Forge file format : "{forge_file_version}"')
            forge_file.seek(file_data_header_offset + 36)
            file_data_offset = struct.unpack('<q', forge_file.read(8))[0]
            forge_file.seek(file_data_offset)
            # File Data
            index_count, index_table_offset, file_data_offset2, name_table_offset, raw_data_table_offset = struct.unpack('<i4x2q8x2q', forge_file.read(48))
            forge_file.seek(index_table_offset)
            index_table: numpy.ndarray = numpy.fromfile(
                forge_file,
                [
                    ('raw_data_offset', numpy.uint64),
                    ('file_id', numpy.uint64),
                    ('raw_data_size', numpy.uint32)
                ],
                index_count
            )
            forge_file.seek(name_table_offset)
            name_table: numpy.ndarray = numpy.fromfile(
                forge_file,
                [
                    ('raw_data_size', numpy.uint32),
                    ('', numpy.uint64),
                    ('', numpy.uint32),
                    ('file_type', numpy.uint32),
                    ('', numpy.uint64),
                    ('', numpy.uint32),  # next file count
                    ('', numpy.uint32),  # previous file count
                    ('', numpy.uint32),
                    ('', numpy.uint32),  # timestamp
                    ('file_name', 'S128'),
                    ('', numpy.uint32),
                    ('', numpy.uint32),
                    ('', numpy.uint32),
                    ('', numpy.uint32),
                    ('', numpy.uint32)
                ],
                index_count
            )
            assert numpy.array_equal(index_table['raw_data_size'], name_table['raw_data_size']), "The duplicated raw data sizes do not match"

            file_names = name_table["file_name"].astype(str)
            return dict(zip(
                index_table["file_id"],
                zip(name_table["file_type"].tolist(), file_names)
            )), dict(zip(
                index_table["file_id"],
                index_table[["raw_data_offset", "raw_data_size"]].tolist()
            ))

    @staticmethod
    def _read_compressed_data_section(raw_data_chunk: BytesIO) -> Tuple[int, List[bytes]]:
        """This is a helper function used in decompression"""
        raw_data_chunk.seek(2, 1)  # 01 00
        compression_type = ord(raw_data_chunk.read(1))
        raw_data_chunk.seek(3, 1)  # 00 80 00
        format_version = ord(raw_data_chunk.read(1))
        if format_version == 0:
            uncompressed_data_list = []
            extra_metadata = b"\x01"
            while extra_metadata:
                extra_metadata = raw_data_chunk.read(1)
                if not extra_metadata:
                    continue
                if extra_metadata == b"\x00":
                    compressed_size = struct.unpack("<I", raw_data_chunk.read(4))[0]
                    # uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
                    uncompressed_data_list.append(raw_data_chunk.read(compressed_size))  # TODO check if this is actually compressed
                elif extra_metadata == b"\x01":
                    compressed_size, uncompressed_size, _ = struct.unpack("<3I", raw_data_chunk.read(12))
                    uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
                else:
                    raise Exception(f"Extra metadata byte {extra_metadata} is not recognised")

        elif format_version == 128:
            comp_block_count = struct.unpack("<I", raw_data_chunk.read(4))[0]
            size_table = numpy.frombuffer(raw_data_chunk.read(comp_block_count * 2 * 2), '<u2').reshape(-1, 2).tolist()  # 'uncompressed_size', 'compressed_size'
            uncompressed_data_list = []
            for uncompressed_size, compressed_size in size_table:
                raw_data_chunk.seek(4, 1)  # I think this is the hash of the data
                uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
        else:
            raise Exception('Format version not known. Please let the creator know where you found this.')

        return format_version, uncompressed_data_list

    def get_decompressed_data_file(self, data_file_id: DataFileIdentifier) -> bytes:
        """Get the decompressed bytes of the datafile.
        Use get_decompressed_files to have the data unpacked into individual files.
        """
        uncompressed_data_list = []

        raw_data_chunk = BytesIO(self.get_compressed_data_file(data_file_id))
        header = raw_data_chunk.read(8)
        if header == CompressionMarker:  # if compressed
            format_version, uncompressed_data_list = self._read_compressed_data_section(raw_data_chunk)
            if format_version == 128:
                if raw_data_chunk.read(8) == CompressionMarker:
                    _, uncompressed_data_list_ = self._read_compressed_data_section(raw_data_chunk)
                    uncompressed_data_list += uncompressed_data_list_
                else:
                    raise Exception('Compression Issue. Second compression block not found')
            if raw_data_chunk.read():
                raise Exception('Compression Issue. More data found')
        else:
            raw_data_chunk_rest = header + raw_data_chunk.read()
            if CompressionMarker in raw_data_chunk_rest:
                raise Exception('Compression Issue')
            uncompressed_data_list.append(raw_data_chunk_rest)  # The file is not compressed

        return b''.join(uncompressed_data_list)

    def get_decompressed_files(self, data_file_id: DataFileIdentifier) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            Optional[bytes]
        ]
    ]:
        """Get the data file unpacked into individual files"""
        uncompressed_data = self.get_decompressed_data_file(data_file_id)
        if data_file_id in self.NonContainerDataFiles:
            data_file = self.get_data_file(data_file_id)
            return {
                data_file_id: (data_file.resource_type, data_file.name, uncompressed_data)
            }

        else:
            files = {}
            uncompressed_data = BytesIO(uncompressed_data)

            file_count = struct.unpack("<H", uncompressed_data.read(2))[0]
            index_table = []
            for _ in range(file_count):
                index_table.append(
                    struct.unpack('<QIH', uncompressed_data.read(14))
                )  # file_id, data_size (file_size + header), extra16_count (for next line)
                uncompressed_data.seek(index_table[-1][2] * 2, 1)
            for index in range(file_count):
                file_type, file_size, file_name_size = struct.unpack('<3I', uncompressed_data.read(12))
                file_id = index_table[index][0]
                file_name = uncompressed_data.read(file_name_size).decode("utf-8")
                check_byte = ord(uncompressed_data.read(1))
                if check_byte == 1:
                    uncompressed_data.seek(3, 1)
                    unk_count = struct.unpack("<I", uncompressed_data.read(4))[0]
                    uncompressed_data.seek(12 * unk_count, 1)
                elif check_byte != 0:
                    raise Exception('Either something has gone wrong or a new value has been found here')

                raw_file = uncompressed_data.read(file_size)

                files[file_id] = (file_type, file_name, raw_file)
            return files
