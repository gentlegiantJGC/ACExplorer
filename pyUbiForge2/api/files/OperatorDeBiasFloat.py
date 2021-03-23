from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorDeBiasFloat(SubclassBaseFile):
    ResourceType = 0x2B203396
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
