from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorDot3(SubclassBaseFile):
    ResourceType = 0xF3335CD4
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

