from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionUnlockHudItem(SubclassBaseFile):
    ResourceType = 0x7686C438
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

