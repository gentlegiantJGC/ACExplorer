from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class DebugOperator(SubclassBaseFile):
    ResourceType = 0xA9993151
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

