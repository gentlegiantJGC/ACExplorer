from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionQuestItemList(SubclassBaseFile):
    ResourceType = 0xC44E80E6
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
