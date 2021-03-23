from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionMoney(SubclassBaseFile):
    ResourceType = 0xDB467822
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
