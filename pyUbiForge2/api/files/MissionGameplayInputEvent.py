from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayInputEvent(SubclassBaseFile):
    ResourceType = 0x926C58CE
    ParentResourceType = _Event.ResourceType
    parent: _Event
