from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionDLCMapMarker(SubclassBaseFile):
    ResourceType = 0x6978B2F0
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

