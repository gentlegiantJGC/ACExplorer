from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WitnessPlayerEventSeed(SubclassBaseFile):
    ResourceType = 0x86C628CC
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
