from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatSquareRoot(SubclassBaseFile):
    ResourceType = 0xF4D3248A
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
