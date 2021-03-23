from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionOnRetryEvent(SubclassBaseFile):
    ResourceType = 0xCCBE9F9A
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

