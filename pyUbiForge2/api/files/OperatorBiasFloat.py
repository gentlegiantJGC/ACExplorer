from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorBiasFloat(SubclassBaseFile):
    ResourceType = 0x63BD38AD
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
