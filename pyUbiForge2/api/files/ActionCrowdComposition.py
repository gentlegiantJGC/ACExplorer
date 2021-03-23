from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionCrowdComposition(SubclassBaseFile):
    ResourceType = 0x047F2A30
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

