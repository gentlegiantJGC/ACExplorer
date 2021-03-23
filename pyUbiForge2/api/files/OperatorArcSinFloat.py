from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorArcSinFloat(SubclassBaseFile):
    ResourceType = 0x92258332
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
