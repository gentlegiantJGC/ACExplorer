from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimationEventSeed import AIAnimationEventSeed as _AIAnimationEventSeed


class ThrowMoneyEventSeed(SubclassBaseFile):
    ResourceType = 0xEE5BB1AF
    ParentResourceType = _AIAnimationEventSeed.ResourceType
    parent: _AIAnimationEventSeed
