from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionFlythrough(SubclassBaseFile):
    ResourceType = 0xA0FBBDA3
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
