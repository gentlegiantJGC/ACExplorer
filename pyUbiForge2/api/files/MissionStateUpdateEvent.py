from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionStateUpdateEvent(SubclassBaseFile):
    ResourceType = 0x8DA67054
    ParentResourceType = _Event.ResourceType
    parent: _Event
