from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorMultiply(SubclassBaseFile):
    ResourceType = 0x36E93FDF
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
