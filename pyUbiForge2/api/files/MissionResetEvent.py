from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionResetEvent(SubclassBaseFile):
    ResourceType = 0xCEBAF67E
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent
