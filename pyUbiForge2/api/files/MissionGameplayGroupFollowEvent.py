from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayGroupFollowEvent(SubclassBaseFile):
    ResourceType = 0xEC7D575B
    ParentResourceType = _Event.ResourceType
    parent: _Event
