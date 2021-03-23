from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionDecipherCodex(SubclassBaseFile):
    ResourceType = 0xDF8DCE36
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

