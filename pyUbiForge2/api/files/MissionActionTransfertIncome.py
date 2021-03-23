from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionTransfertIncome(SubclassBaseFile):
    ResourceType = 0x55FCE048
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
