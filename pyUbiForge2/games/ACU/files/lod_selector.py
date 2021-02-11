from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('01437462')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(1)
        file.read_file_id()
        file.out_file_write('\n')
        self._lod = []
        for _ in range(5):
            ending0 = file.read_uint_8()
            if ending0 == 0:
                self._lod.append(file.read_file())
            elif ending0 == 3:
                self._lod.append(None)
            else:
                raise Exception()

    def __getitem__(self, index: int):
        return self._lod[index]
