from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFracFloat(SubclassBaseFile):
    ResourceType = 0x1C564647
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

