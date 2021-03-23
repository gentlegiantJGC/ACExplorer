from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class BloodSplatterEventSeed(SubclassBaseFile):
    ResourceType = 0x0DDBFECD
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
