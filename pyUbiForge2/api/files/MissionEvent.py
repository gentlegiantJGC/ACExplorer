from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionEvent(SubclassBaseFile):
    ResourceType = 0x9639224F
    ParentResourceType = _Event.ResourceType
    parent: _Event
