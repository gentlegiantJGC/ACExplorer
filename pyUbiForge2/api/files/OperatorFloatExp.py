from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatExp(SubclassBaseFile):
    ResourceType = 0x40EB69A1
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
