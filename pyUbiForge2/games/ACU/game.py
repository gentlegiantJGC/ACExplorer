from pyUbiForge2.api import BaseGame, BaseFile
from pyUbiForge2.api.file_object import FileDataWrapper

from .forge import ACUForge


class ACUGame(BaseGame):
    ForgeClass = ACUForge
    GameIdentifier = "ACU"
    FileIDType = "Q"
    ResourceType = "I"

    def read_file(self, file: FileDataWrapper) -> BaseFile:
        pass
