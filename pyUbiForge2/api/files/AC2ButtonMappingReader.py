from pyUbiForge2.api.game import SubclassBaseFile
from .PadInputReader import PadInputReader as _PadInputReader


class AC2ButtonMappingReader(SubclassBaseFile):
    ResourceType = 0xD3AD3DB9
    ParentResourceType = _PadInputReader.ResourceType
    parent: _PadInputReader
