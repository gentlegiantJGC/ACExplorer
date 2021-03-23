from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionTimeOfDay(SubclassBaseFile):
    ResourceType = 0x23DBD635
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
