from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AIAnimationEvent(SubclassBaseFile):
    ResourceType = 0xF9BFCB7C
    ParentResourceType = _Event.ResourceType
    parent: _Event
