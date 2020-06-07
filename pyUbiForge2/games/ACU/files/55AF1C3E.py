from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('55AF1C3E')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(2)
        count1 = file.read_uint_32()
        for _ in range(count1):
            file.read_bytes(41)
        count2 = file.read_uint_32()
        file.read_bytes(12 * count2)
        for _ in range(2):
            file.read_file()
        file.out_file_write('\n')

        """
        file.read_bytes(2)
        count1 = file.read_uint_32()
    
        if count1 > 100:
            logging.warning('error reading unknown file type')
            # convert to an actual logger
            return fileContainer
        for _ in range(count1):
            file.read_file()
        file.out_file_write('\n')
    
        count2 = file.read_uint_32()
        if count2 > 100:
            logging.warning('error reading unknown file type')
            # convert to an actual logger
            return fileContainer
        for _ in range(count2):
            readStr(fIn, fOut, 12)
        file.out_file_write('\n')
        """
