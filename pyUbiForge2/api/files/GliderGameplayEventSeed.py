from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class GliderGameplayEventSeed(SubclassBaseFile):
    ResourceType = 0x0B42DFAF
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

