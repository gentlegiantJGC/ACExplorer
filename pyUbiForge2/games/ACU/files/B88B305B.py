from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import logging


@register_file_reader('B88B305B')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        check = file.read_uint_8()
        if check == 1:
            file.read_bytes(1)
            file.read_file_id()
        elif check == 3:
            file.read_bytes(9)
        else:
            logging.warning(f'Expected check to be 1 or 3 but got {check}')
            raise Exception

        file.read_bytes(1)

        check = file.read_uint_8()
        if check == 1:
            file.read_bytes(1)
            file.read_file_id()
        elif check == 3:
            file.read_bytes(9)
        else:
            logging.warning(f'Expected check to be 1 or 3 but got {check}')
            raise Exception
