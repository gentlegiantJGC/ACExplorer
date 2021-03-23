from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionGameplayPupetteerAction(SubclassBaseFile):
    ResourceType = 0x589538B3
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
