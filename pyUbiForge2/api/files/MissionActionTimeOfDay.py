from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionTimeOfDay(SubclassBaseFile):
    ResourceType = 0xB53B8AD3
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
