from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimationEvent import AIAnimationEvent as _AIAnimationEvent


class AnimAssassinationEvent(SubclassBaseFile):
    ResourceType = 0x28C6E4EE
    ParentResourceType = _AIAnimationEvent.ResourceType
    parent: _AIAnimationEvent
