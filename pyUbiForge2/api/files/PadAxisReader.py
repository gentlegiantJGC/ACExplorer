from pyUbiForge2.api.game import SubclassBaseFile
from .PadInputReader import PadInputReader as _PadInputReader


class PadAxisReader(SubclassBaseFile):
    ResourceType = 0x0772E5F2
    ParentResourceType = _PadInputReader.ResourceType
    parent: _PadInputReader
