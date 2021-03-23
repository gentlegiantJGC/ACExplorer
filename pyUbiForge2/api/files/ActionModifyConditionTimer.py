from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionModifyConditionTimer(SubclassBaseFile):
    ResourceType = 0xD981128D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
