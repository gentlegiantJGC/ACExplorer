from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorReflect(SubclassBaseFile):
    ResourceType = 0xA760E24D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
