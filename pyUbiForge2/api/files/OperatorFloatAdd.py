from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatAdd(SubclassBaseFile):
    ResourceType = 0xBB4F485D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
