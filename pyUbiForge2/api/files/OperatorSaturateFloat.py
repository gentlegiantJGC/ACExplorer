from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSaturateFloat(SubclassBaseFile):
    ResourceType = 0x584B953A
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

