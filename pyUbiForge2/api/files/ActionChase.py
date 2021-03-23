from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionChase(SubclassBaseFile):
    ResourceType = 0xFA64505F
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

