from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionOnRestartEvent(SubclassBaseFile):
    ResourceType = 0x51CD2A81
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent
