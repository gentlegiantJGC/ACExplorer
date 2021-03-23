from pyUbiForge2.api.game import SubclassBaseFile
from .StartTrigger import StartTrigger as _StartTrigger


class ConditionTrigger(SubclassBaseFile):
    ResourceType = 0xAC44A853
    ParentResourceType = _StartTrigger.ResourceType
    parent: _StartTrigger
