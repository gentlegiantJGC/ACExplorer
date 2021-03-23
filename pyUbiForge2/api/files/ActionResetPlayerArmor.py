from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionResetPlayerArmor(SubclassBaseFile):
    ResourceType = 0x8AF1F4D1
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
