from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionPauseConditionTimer(SubclassBaseFile):
    ResourceType = 0x9DC79785
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

