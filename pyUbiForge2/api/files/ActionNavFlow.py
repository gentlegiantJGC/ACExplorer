from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionNavFlow(SubclassBaseFile):
    ResourceType = 0x67A92385
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

