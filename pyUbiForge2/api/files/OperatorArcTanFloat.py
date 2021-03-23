from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorArcTanFloat(SubclassBaseFile):
    ResourceType = 0xAB0FC44C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

