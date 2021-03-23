from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEntityWorldPosition(SubclassBaseFile):
    ResourceType = 0x818F8014
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

