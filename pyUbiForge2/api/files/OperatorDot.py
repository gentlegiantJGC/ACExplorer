from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorDot(SubclassBaseFile):
    ResourceType = 0x8547EC07
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

