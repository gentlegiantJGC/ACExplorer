from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class SceneEventSeed(SubclassBaseFile):
    ResourceType = 0x609C4E1F
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

