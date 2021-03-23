from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorLength(SubclassBaseFile):
    ResourceType = 0x3C9802CB
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

