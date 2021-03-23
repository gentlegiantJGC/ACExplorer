from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSaturateVector(SubclassBaseFile):
    ResourceType = 0x5D9618E9
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

