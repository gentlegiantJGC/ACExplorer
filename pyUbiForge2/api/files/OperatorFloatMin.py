from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatMin(SubclassBaseFile):
    ResourceType = 0xE72E266A
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
