from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatSub(SubclassBaseFile):
    ResourceType = 0x1E57B966
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
