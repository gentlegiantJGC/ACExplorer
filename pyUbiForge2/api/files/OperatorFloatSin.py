from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatSin(SubclassBaseFile):
    ResourceType = 0xF196A810
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
