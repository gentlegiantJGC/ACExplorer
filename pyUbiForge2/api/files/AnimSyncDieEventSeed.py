from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AnimSyncDieEventSeed(SubclassBaseFile):
    ResourceType = 0x483398A0
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

