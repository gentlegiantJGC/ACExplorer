from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy
import logging


@register_file_reader('0984415E')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id, resource_type)
        check_byte = file.read_uint_8()  # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
        if check_byte == 0:
            for _ in range(2):
                file.read_file()
        file.out_file_write('Transformation Matrix\n')
        self.transformation_matrix = file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')

        file.out_file_write('\n')
        count1 = file.read_uint_32()
        if count1 > 10000:
            logging.warning('error reading entity file')
            # convert to an actual logger
            raise Exception

        self.nested_files = []

        for _ in range(count1):
            file.out_file_write('\n')
            file.indent()
            if file.read_bytes(2) not in [b'\x04\x00', b'\x00\x01']:  # 04 00
                raise Exception
            file.indent(-1)

            self.nested_files.append(file.read_file())

        # float * 7

        # 37 bytes
        # 2 bytes
        # float

        # bouding box
        # id
        # type
        # float32 * 6
        # int32

        # entity descriptor
        # 19 bytes

        file.out_file_write('\n')

        file.read_bytes(43)

        # data layer filter
        # 4 count, more data in here sometimes
        for _ in range(3):
            file.read_file()

        # 03 end file?
        check_byte_2 = file.read_uint_8()
        if check_byte_2 == 0:
            file.read_file()
        elif check_byte_2 != 3:
            raise Exception
        file.out_file_write('\n')
