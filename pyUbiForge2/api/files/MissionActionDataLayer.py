from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionDataLayer(SubclassBaseFile):
    ResourceType = 0xA6B3603A
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
