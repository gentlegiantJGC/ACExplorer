from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class RandomSource(SubclassBaseFile):
    ResourceType = 0xFE20EBBB
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

