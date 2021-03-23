from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorCross(SubclassBaseFile):
    ResourceType = 0x6A1ABA5C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

