from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AIAnimationEventSeed(SubclassBaseFile):
    ResourceType = 0xFF9AD272
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
