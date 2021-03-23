from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionPlayerQuestItemList(SubclassBaseFile):
    ResourceType = 0x275D51E9
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
