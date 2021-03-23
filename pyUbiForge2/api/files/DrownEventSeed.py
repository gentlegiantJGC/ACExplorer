from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class DrownEventSeed(SubclassBaseFile):
    ResourceType = 0xDA25CF71
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

