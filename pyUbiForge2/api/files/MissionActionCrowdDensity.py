from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionCrowdDensity(SubclassBaseFile):
    ResourceType = 0x8BD2444B
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

