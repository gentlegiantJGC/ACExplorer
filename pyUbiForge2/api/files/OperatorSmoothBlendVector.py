from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSmoothBlendVector(SubclassBaseFile):
    ResourceType = 0x22242A42
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

