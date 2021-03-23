from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader2 import InputReader2 as _InputReader2


class MultiplicativeAndReader(SubclassBaseFile):
    ResourceType = 0x426075E2
    ParentResourceType = _InputReader2.ResourceType
    parent: _InputReader2
