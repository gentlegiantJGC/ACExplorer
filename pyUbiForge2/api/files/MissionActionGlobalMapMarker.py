from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionGlobalMapMarker(SubclassBaseFile):
    ResourceType = 0x31ABA02E
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
