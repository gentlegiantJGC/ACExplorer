from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class HudWeaponSelectComponent(SubclassBaseFile):
    ResourceType = 0x776C6B23
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

