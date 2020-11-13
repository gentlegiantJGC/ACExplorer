from typing import Tuple, Dict, List
import struct
import numpy
from io import BytesIO

from pyUbiForge2.api import BaseForge
from pyUbiForge2.api.data_types import (
    FileIdentifier,
    FileResourceType,
    FileName,
)
from pyUbiForge2.util.compression import decompress


class ACUForge(BaseForge):
    NonContainerDataFiles = {16, 145}

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
