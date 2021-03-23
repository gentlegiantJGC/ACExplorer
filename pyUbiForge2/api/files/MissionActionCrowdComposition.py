from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionCrowdComposition(SubclassBaseFile):
    ResourceType = 0xAFBC0836
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

