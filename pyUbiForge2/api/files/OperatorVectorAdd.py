from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorAdd(SubclassBaseFile):
    ResourceType = 0x61A0FD1C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

