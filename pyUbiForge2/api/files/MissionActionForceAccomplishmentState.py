from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionForceAccomplishmentState(SubclassBaseFile):
    ResourceType = 0x6502A15B
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
