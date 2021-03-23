from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader import InputReader as _InputReader


class BooleanReader(SubclassBaseFile):
    ResourceType = 0x2BF969C4
    ParentResourceType = _InputReader.ResourceType
    parent: _InputReader
