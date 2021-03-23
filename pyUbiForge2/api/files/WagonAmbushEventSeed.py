from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WagonAmbushEventSeed(SubclassBaseFile):
    ResourceType = 0xCEF841F6
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

