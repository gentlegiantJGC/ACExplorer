from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class AndTrigger(SubclassBaseFile):
    ResourceType = 0x1A481920
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger
