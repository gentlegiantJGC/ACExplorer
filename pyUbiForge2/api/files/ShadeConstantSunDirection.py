from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantSunDirection(SubclassBaseFile):
    ResourceType = 0xBE260850
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
