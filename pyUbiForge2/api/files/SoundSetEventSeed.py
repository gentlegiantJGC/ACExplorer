from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class SoundSetEventSeed(SubclassBaseFile):
    ResourceType = 0x92332333
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
