from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionResponseEvent(SubclassBaseFile):
    ResourceType = 0x2F586BD1
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent
