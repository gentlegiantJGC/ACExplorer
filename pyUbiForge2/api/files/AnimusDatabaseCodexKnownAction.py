from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class AnimusDatabaseCodexKnownAction(SubclassBaseFile):
    ResourceType = 0x908001DD
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

