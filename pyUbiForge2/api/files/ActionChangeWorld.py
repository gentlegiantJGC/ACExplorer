from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionChangeWorld(SubclassBaseFile):
    ResourceType = 0x6D922078
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
