from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantSunColor(SubclassBaseFile):
    ResourceType = 0x533B2EE5
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

