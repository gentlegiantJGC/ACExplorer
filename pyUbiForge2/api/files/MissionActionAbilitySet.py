from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionAbilitySet(SubclassBaseFile):
    ResourceType = 0xC0091302
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

