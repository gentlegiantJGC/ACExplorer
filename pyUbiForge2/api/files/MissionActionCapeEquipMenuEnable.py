from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionCapeEquipMenuEnable(SubclassBaseFile):
    ResourceType = 0xC56E23D1
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
