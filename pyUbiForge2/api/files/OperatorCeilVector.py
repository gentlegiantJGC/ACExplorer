from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorCeilVector(SubclassBaseFile):
    ResourceType = 0x7843871B
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

