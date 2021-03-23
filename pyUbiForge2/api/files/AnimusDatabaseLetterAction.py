from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class AnimusDatabaseLetterAction(SubclassBaseFile):
    ResourceType = 0x41489670
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
