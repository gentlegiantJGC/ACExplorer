from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WagonDamageEventSeed(SubclassBaseFile):
    ResourceType = 0x1435511F
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
