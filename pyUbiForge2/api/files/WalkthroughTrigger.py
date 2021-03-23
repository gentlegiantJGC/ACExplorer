from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class WalkthroughTrigger(SubclassBaseFile):
    ResourceType = 0x2B4970B6
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger
