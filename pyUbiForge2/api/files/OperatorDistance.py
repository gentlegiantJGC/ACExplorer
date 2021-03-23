from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorDistance(SubclassBaseFile):
    ResourceType = 0x1BD6BAB4
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

