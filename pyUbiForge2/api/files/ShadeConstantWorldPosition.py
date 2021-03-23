from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantWorldPosition(SubclassBaseFile):
    ResourceType = 0x0702E026
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
