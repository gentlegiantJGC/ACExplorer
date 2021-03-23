from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPSPItemsUnlock(SubclassBaseFile):
    ResourceType = 0x56D4234C
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
