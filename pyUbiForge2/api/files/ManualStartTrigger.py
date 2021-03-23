from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class ManualStartTrigger(SubclassBaseFile):
    ResourceType = 0xF633A53F
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger

