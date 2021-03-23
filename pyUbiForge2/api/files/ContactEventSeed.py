from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class ContactEventSeed(SubclassBaseFile):
    ResourceType = 0x993AB038
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

