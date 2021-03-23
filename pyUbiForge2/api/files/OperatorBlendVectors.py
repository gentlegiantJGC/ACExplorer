from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorBlendVectors(SubclassBaseFile):
    ResourceType = 0x52089548
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

