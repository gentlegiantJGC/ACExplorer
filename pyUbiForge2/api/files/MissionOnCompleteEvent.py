from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionOnCompleteEvent(SubclassBaseFile):
    ResourceType = 0xF18109F3
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

