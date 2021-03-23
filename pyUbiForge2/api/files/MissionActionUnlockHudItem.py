from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionUnlockHudItem(SubclassBaseFile):
    ResourceType = 0xA726C895
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

