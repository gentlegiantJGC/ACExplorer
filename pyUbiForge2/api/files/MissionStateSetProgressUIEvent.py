from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateSetProgressUIEvent(SubclassBaseFile):
    ResourceType = 0x6B8B6E58
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
