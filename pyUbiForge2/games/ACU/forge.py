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
    NonContainerDataFiles = {16, 145}

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

    def _decompress_data_file(self, compressed_bytes: bytes) -> bytes:
        uncompressed_data_list = []

        raw_data_chunk = BytesIO(compressed_bytes)
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

    def _unpack_decompressed_data_file(self, decompressed_bytes: bytes) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            bytes
        ]
    ]:
        files = {}
        uncompressed_data = BytesIO(decompressed_bytes)

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
