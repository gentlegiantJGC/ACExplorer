from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class AnimusDatabaseAction(SubclassBaseFile):
    ResourceType = 0xC5A962D2
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

