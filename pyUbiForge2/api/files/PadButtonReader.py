from pyUbiForge2.api.game import SubclassBaseFile
from .PadInputReader import PadInputReader as _PadInputReader


class PadButtonReader(SubclassBaseFile):
    ResourceType = 0x2F01F1A1
    ParentResourceType = _PadInputReader.ResourceType
    parent: _PadInputReader
