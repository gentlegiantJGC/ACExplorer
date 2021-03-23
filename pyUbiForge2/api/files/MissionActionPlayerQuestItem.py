from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPlayerQuestItem(SubclassBaseFile):
    ResourceType = 0x4CD1620A
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

