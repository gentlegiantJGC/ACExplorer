from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPlayerHealth(SubclassBaseFile):
    ResourceType = 0x874FB5A9
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

