from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader2 import InputReader2 as _InputReader2


class AdditiveAndReader(SubclassBaseFile):
    ResourceType = 0xF379397E
    ParentResourceType = _InputReader2.ResourceType
    parent: _InputReader2

