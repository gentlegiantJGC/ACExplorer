from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class PauseMenuComponent(SubclassBaseFile):
    ResourceType = 0xC8826E93
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
