from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPauseConditionTimer(SubclassBaseFile):
    ResourceType = 0x3C953EB6
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
