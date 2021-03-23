from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantScreenPosition(SubclassBaseFile):
    ResourceType = 0x22235BC0
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

