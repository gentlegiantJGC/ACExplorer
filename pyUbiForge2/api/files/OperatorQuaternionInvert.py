from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorQuaternionInvert(SubclassBaseFile):
    ResourceType = 0x58E739B3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
