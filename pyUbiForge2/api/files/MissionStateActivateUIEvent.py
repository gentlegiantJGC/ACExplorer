from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateActivateUIEvent(SubclassBaseFile):
    ResourceType = 0x2464077B
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
