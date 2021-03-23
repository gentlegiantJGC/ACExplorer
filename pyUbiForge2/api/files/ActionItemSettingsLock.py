from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionItemSettingsLock(SubclassBaseFile):
    ResourceType = 0xC5B5B3C6
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
