from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionSkipEvent(SubclassBaseFile):
    ResourceType = 0x38153C1D
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

