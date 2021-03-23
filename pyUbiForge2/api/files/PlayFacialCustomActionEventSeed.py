from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class PlayFacialCustomActionEventSeed(SubclassBaseFile):
    ResourceType = 0x60790DD0
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
