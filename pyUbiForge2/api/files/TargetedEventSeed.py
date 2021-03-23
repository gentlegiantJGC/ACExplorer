from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class TargetedEventSeed(SubclassBaseFile):
    ResourceType = 0x31E53393
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

