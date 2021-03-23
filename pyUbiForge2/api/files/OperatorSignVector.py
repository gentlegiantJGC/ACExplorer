from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSignVector(SubclassBaseFile):
    ResourceType = 0x3BCCF6FC
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

