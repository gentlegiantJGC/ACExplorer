from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class HideAction(SubclassBaseFile):
    ResourceType = 0xE2AAFDD9
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

