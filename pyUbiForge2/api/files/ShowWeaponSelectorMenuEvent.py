from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ShowWeaponSelectorMenuEvent(SubclassBaseFile):
    ResourceType = 0x519BA677
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
