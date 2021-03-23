from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionChangeWorld(SubclassBaseFile):
    ResourceType = 0x076BFF2D
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

