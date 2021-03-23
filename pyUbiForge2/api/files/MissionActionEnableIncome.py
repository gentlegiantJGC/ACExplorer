from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionEnableIncome(SubclassBaseFile):
    ResourceType = 0x2949B280
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

