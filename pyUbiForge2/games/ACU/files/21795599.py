from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('21795599')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        for length in [2, 2, 1, 1, 4, 2, 2]:
            total_count = file.read_uint_32()
            file.indent()
            file.read_bytes(total_count * length)
            file.indent(-1)
        found_count = 0
        empty_count = 0
        filled_count = 0
        # probably not right but this seems to work
        while found_count < total_count or empty_count != filled_count + 1:
            check_byte = file.read_uint_8()
            if check_byte == 0:
                sub_file_container = file.read_file()
                found_count += sub_file_container.count
                if sub_file_container.count > 0:
                    filled_count += 1
                else:
                    empty_count += 1

            elif check_byte == 3:
                filled_count += 1
                continue
            else:
                raise Exception(f'{__name__}: check_byte is not in 0, 3')
        file.read_bytes(8)
        count = file.read_uint_32()
        for _ in range(count):
            check_byte = file.read_bytes(1)
            file.read_file()
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(4)
        file.read_bytes(1)
        for _ in range(7):
            file.read_bytes(4)
        file.read_file()
