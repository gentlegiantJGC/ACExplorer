from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AnimusDatabaseTriggerEventSeed(SubclassBaseFile):
    ResourceType = 0xA0ED9700
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

