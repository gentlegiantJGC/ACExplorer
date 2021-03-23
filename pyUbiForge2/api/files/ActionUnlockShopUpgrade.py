from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionUnlockShopUpgrade(SubclassBaseFile):
    ResourceType = 0xD5990E83
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
