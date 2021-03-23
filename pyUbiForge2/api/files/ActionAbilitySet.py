from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionAbilitySet(SubclassBaseFile):
    ResourceType = 0x89F6B413
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

