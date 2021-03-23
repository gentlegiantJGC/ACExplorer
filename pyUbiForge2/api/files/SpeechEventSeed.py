from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class SpeechEventSeed(SubclassBaseFile):
    ResourceType = 0xD69AFE1D
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
