from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionSetPlayerRank(SubclassBaseFile):
    ResourceType = 0x1145936D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
