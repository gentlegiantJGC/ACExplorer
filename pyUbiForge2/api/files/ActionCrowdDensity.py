from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionCrowdDensity(SubclassBaseFile):
    ResourceType = 0x90B918EF
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

