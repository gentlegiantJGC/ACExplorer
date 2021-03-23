from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionSetPlayerRank(SubclassBaseFile):
    ResourceType = 0xC0E59FC0
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

