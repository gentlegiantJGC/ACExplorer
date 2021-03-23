from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionActivateEntity(SubclassBaseFile):
    ResourceType = 0x6D948A6B
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

