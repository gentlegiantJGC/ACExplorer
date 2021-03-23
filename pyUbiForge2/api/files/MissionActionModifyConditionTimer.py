from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionModifyConditionTimer(SubclassBaseFile):
    ResourceType = 0x66F02132
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
