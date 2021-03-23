from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionResetPlayerArmor(SubclassBaseFile):
    ResourceType = 0x2132D6D7
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
