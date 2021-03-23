from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class MissionGameplayPupetteerEventSeed(SubclassBaseFile):
    ResourceType = 0x13803E35
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
