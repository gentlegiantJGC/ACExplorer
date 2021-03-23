from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorBiasVector(SubclassBaseFile):
    ResourceType = 0x33C6E8A3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

