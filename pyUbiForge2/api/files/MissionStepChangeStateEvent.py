from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionStepChangeStateEvent(SubclassBaseFile):
    ResourceType = 0xA62612C5
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent
