from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionFailedEvent(SubclassBaseFile):
    ResourceType = 0x16701666
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

