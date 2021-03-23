from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionActivatorMenu(SubclassBaseFile):
    ResourceType = 0x63BBD87C
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
