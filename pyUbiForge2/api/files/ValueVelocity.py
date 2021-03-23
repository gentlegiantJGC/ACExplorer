from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ValueVelocity(SubclassBaseFile):
    ResourceType = 0x6B3A6B17
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
