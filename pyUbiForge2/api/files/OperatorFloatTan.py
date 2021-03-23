from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatTan(SubclassBaseFile):
    ResourceType = 0x3C00349D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

