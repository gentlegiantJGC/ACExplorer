from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class HudGroupInfoComponent(SubclassBaseFile):
    ResourceType = 0x3B7F9413
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

