from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorFloatMultiply(SubclassBaseFile):
    ResourceType = 0x78FB1B01
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

