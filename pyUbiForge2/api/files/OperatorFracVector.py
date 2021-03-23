from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFracVector(SubclassBaseFile):
    ResourceType = 0x736608BB
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
