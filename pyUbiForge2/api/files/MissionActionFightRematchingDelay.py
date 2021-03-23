from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionFightRematchingDelay(SubclassBaseFile):
    ResourceType = 0x1EB4DC2B
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

