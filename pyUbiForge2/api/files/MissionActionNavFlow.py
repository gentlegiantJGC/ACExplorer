from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionNavFlow(SubclassBaseFile):
    ResourceType = 0xF0645C83
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
