from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionItemSettingsPrice(SubclassBaseFile):
    ResourceType = 0xB6FD3464
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
