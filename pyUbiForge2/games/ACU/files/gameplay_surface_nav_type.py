from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import logging


@register_file_reader('1C4B22AA')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(5)  # zeros
    # count = file.read_uint_8()
    # if count > 0:
    # 	file.read_bytes(3)
    # 	for _ in range(count):
    # 		file.read_file()
    # 	file.read_bytes(4)
    #
    # b = file.read_uint_8()
    # if b == 3:
    # 	file.read_bytes(9)
    # 	file.read_bytes(4 * file.read_uint_32())
    # elif b == 5:
    # 	file.read_file_id()
    # 	file.read_bytes(5)
    # 	file.read_file_id()
    # else:
    # 	logging.warning('value is not 3 or 5 I don\'t know how to deal with this')
