from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionFastTravel(SubclassBaseFile):
    ResourceType = 0x2DF1490A
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
