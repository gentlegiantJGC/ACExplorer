from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionOnCancelEvent(SubclassBaseFile):
    ResourceType = 0xE298511F
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

