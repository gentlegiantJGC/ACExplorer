from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatDiv(SubclassBaseFile):
    ResourceType = 0xFB9385B3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

