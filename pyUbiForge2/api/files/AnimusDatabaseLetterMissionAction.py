from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class AnimusDatabaseLetterMissionAction(SubclassBaseFile):
    ResourceType = 0x0DB1E548
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

