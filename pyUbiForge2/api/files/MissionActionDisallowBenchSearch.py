from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionDisallowBenchSearch(SubclassBaseFile):
    ResourceType = 0x2FA15E23
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
