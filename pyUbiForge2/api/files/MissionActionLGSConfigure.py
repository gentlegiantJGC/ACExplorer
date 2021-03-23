from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionLGSConfigure(SubclassBaseFile):
    ResourceType = 0x2B667A23
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
