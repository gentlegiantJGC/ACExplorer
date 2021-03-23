from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionDisallowBenchSearch(SubclassBaseFile):
    ResourceType = 0x8EF3F710
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

