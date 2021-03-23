from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AnimTimingEventSeed(SubclassBaseFile):
    ResourceType = 0xAB66DA61
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
