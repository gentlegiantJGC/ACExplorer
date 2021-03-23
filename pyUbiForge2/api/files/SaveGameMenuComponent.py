from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class SaveGameMenuComponent(SubclassBaseFile):
    ResourceType = 0x00782DCB
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

