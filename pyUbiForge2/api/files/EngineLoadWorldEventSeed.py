from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class EngineLoadWorldEventSeed(SubclassBaseFile):
    ResourceType = 0xABF6A8F3
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

