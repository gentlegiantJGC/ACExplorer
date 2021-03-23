from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatAbs(SubclassBaseFile):
    ResourceType = 0x6EC66A1C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
