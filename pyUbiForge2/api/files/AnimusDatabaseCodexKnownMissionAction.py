from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class AnimusDatabaseCodexKnownMissionAction(SubclassBaseFile):
    ResourceType = 0x6C230CFB
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
