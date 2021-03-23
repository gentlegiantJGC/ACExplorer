from pyUbiForge2.api.game import SubclassBaseFile
from .FXPack import FXPack as _FXPack


class CannonFXPack(SubclassBaseFile):
    ResourceType = 0xE37542B7
    ParentResourceType = _FXPack.ResourceType
    parent: _FXPack
