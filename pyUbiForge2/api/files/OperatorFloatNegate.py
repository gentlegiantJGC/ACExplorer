from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatNegate(SubclassBaseFile):
    ResourceType = 0xA4FB41FF
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

