from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class HudAnimusDatabaseActivateUIEvent(SubclassBaseFile):
    ResourceType = 0xF604EE92
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
