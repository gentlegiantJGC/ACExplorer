from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionFlythrough(SubclassBaseFile):
    ResourceType = 0xE9041AB2
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

