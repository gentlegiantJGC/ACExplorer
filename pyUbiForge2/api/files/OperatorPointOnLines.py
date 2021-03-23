from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorPointOnLines(SubclassBaseFile):
    ResourceType = 0x306CA167
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
