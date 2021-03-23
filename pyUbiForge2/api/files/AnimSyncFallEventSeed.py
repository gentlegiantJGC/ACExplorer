from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AnimSyncFallEventSeed(SubclassBaseFile):
    ResourceType = 0x1A6ED566
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
