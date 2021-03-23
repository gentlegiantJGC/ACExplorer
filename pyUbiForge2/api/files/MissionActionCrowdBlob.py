from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionCrowdBlob(SubclassBaseFile):
    ResourceType = 0x3E33EFE9
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

