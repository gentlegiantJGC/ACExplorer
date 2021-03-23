from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatInvert(SubclassBaseFile):
    ResourceType = 0x1D685F04
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
