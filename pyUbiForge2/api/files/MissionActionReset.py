from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionReset(SubclassBaseFile):
    ResourceType = 0x4009B158
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

