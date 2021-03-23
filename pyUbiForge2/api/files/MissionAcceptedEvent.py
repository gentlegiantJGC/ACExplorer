from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionAcceptedEvent(SubclassBaseFile):
    ResourceType = 0xF7895050
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

