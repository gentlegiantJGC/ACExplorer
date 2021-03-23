from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class LGSSolvedMissionAction(SubclassBaseFile):
    ResourceType = 0xE4BABE4E
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

