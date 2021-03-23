from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class OrTrigger(SubclassBaseFile):
    ResourceType = 0x41EDA72A
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger

