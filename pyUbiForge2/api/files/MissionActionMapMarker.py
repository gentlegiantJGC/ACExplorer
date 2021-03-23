from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionMapMarker(SubclassBaseFile):
    ResourceType = 0xEA6E53E5
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

