from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionNotoriety(SubclassBaseFile):
    ResourceType = 0x806F4B84
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
