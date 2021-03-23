from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AudioEventSeed(SubclassBaseFile):
    ResourceType = 0x561E06FC
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
