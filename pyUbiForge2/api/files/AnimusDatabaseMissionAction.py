from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class AnimusDatabaseMissionAction(SubclassBaseFile):
    ResourceType = 0x2409B303
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
