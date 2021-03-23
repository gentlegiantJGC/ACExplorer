from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class HudControlsManagerComponent(SubclassBaseFile):
    ResourceType = 0x11A90925
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
