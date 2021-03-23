from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader2 import InputReader2 as _InputReader2


class BooleanOperationInputReader(SubclassBaseFile):
    ResourceType = 0x175ECE5C
    ParentResourceType = _InputReader2.ResourceType
    parent: _InputReader2

