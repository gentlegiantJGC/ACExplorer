from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionChase(SubclassBaseFile):
    ResourceType = 0x8669358C
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

