from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorQuaternionMul(SubclassBaseFile):
    ResourceType = 0xE940B7BD
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

