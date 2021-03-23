from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionFactionStatus(SubclassBaseFile):
    ResourceType = 0x499E42A1
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
