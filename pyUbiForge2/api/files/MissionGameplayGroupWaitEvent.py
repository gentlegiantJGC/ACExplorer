from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayGroupWaitEvent(SubclassBaseFile):
    ResourceType = 0x31CBFA49
    ParentResourceType = _Event.ResourceType
    parent: _Event
