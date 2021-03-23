from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class WorldToScreen(SubclassBaseFile):
    ResourceType = 0x88E15F23
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

