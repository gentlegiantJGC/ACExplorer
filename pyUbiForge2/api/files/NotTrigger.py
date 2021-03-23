from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class NotTrigger(SubclassBaseFile):
    ResourceType = 0x808367C5
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger

