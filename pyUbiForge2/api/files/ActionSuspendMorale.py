from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionSuspendMorale(SubclassBaseFile):
    ResourceType = 0x0E8205E8
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

