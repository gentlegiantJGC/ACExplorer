from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader2 import InputReader2 as _InputReader2


class PadInputReader(SubclassBaseFile):
    ResourceType = 0x1ACF70EF
    ParentResourceType = _InputReader2.ResourceType
    parent: _InputReader2
