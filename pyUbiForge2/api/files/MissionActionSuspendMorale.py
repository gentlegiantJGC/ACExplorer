from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionSuspendMorale(SubclassBaseFile):
    ResourceType = 0xDF220945
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

