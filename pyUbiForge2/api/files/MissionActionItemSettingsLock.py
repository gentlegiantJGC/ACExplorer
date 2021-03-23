from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionItemSettingsLock(SubclassBaseFile):
    ResourceType = 0x6E7691C0
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

