from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class WeaponSelectorMenuComponent(SubclassBaseFile):
    ResourceType = 0x48B13C34
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
