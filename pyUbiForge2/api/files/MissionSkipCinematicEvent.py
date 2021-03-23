from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionSkipCinematicEvent(SubclassBaseFile):
    ResourceType = 0x9997DCD3
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent
