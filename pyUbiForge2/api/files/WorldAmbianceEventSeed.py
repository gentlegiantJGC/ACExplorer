from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WorldAmbianceEventSeed(SubclassBaseFile):
    ResourceType = 0xF190D936
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

