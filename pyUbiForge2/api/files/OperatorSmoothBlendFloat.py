from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorSmoothBlendFloat(SubclassBaseFile):
    ResourceType = 0x80748576
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

