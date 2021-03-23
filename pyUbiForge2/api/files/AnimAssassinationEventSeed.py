from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimationEventSeed import AIAnimationEventSeed as _AIAnimationEventSeed


class AnimAssassinationEventSeed(SubclassBaseFile):
    ResourceType = 0xD4EBDA7D
    ParentResourceType = _AIAnimationEventSeed.ResourceType
    parent: _AIAnimationEventSeed
