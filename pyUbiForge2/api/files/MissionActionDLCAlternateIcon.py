from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionDLCAlternateIcon(SubclassBaseFile):
    ResourceType = 0xBEB787BF
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

