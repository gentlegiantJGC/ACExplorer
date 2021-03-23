from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionFamilyTree(SubclassBaseFile):
    ResourceType = 0x64103B27
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
