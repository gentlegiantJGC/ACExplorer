from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionCrowdBlob(SubclassBaseFile):
    ResourceType = 0xA8D3B30F
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

