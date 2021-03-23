from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionUnlockShopUpgrade(SubclassBaseFile):
    ResourceType = 0x3C516894
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

