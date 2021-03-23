from pyUbiForge2.api.game import SubclassBaseFile
from .FXPack import FXPack as _FXPack


class HumanFXPack(SubclassBaseFile):
    ResourceType = 0xBA42B58E
    ParentResourceType = _FXPack.ResourceType
    parent: _FXPack
