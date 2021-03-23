from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimationEvent import AIAnimationEvent as _AIAnimationEvent


class ThrowMoneyEvent(SubclassBaseFile):
    ResourceType = 0xDFD4F376
    ParentResourceType = _AIAnimationEvent.ResourceType
    parent: _AIAnimationEvent

