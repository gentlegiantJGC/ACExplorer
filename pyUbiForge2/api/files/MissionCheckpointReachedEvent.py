from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionCheckpointReachedEvent(SubclassBaseFile):
    ResourceType = 0x65B72A16
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

