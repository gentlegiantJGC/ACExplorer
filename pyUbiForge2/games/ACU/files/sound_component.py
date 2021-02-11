from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('E8134060')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(2)
        # for _ in range(3):
        for _ in range(2):
            file.read_file()
            # SoundComponent
            # EventSwitchDependencies
        file.read_bytes(10)  # wrong but needs more examples
