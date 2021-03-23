from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class TriggerEventSeed(SubclassBaseFile):
    ResourceType = 0x5C1EE4A0
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
