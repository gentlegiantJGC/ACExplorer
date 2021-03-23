from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorArcCosFloat(SubclassBaseFile):
    ResourceType = 0x32069666
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

