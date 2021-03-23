from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorQuaternionSlerp(SubclassBaseFile):
    ResourceType = 0xF5AB6D54
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
