from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionQuestItem(SubclassBaseFile):
    ResourceType = 0xD045DAE9
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

