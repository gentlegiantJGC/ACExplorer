from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatCos(SubclassBaseFile):
    ResourceType = 0xD8ECC03F
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
