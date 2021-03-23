from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSignFloat(SubclassBaseFile):
    ResourceType = 0x049E4AE0
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
