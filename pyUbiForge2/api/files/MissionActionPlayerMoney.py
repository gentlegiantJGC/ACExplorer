from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPlayerMoney(SubclassBaseFile):
    ResourceType = 0x4B0EE402
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

