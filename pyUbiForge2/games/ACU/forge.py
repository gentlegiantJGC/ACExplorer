from typing import Tuple, Dict, Optional
import logging
import struct
import numpy

from pyUbiForge2.api import BaseForge
from pyUbiForge2.api.data_types import (
    DataFileMetadata,
    DataFileByteLocations,
    DataFileIdentifier,
    FileIdentifier,
    FileResourceType,
    FileName,
)


class ACUForge(BaseForge):
    GameIdentifier = "ACU"

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

    def decompress_data_file(self, data_file_id: DataFileIdentifier, metadata_only=False) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            Optional[bytes]
        ]
    ]:
        raise NotImplementedError
