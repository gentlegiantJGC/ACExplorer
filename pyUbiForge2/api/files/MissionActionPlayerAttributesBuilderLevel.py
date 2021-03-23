from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPlayerAttributesBuilderLevel(SubclassBaseFile):
    ResourceType = 0x6C884ACC
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

