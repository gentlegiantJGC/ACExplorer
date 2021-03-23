from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionAFSMessage(SubclassBaseFile):
    ResourceType = 0xB7E532B1
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
