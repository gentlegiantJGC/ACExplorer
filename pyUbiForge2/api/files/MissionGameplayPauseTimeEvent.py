from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayPauseTimeEvent(SubclassBaseFile):
    ResourceType = 0x22C9F1DE
    ParentResourceType = _Event.ResourceType
    parent: _Event
