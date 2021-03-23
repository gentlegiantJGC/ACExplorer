from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionGlobalMapMarker(SubclassBaseFile):
    ResourceType = 0x23B4FF01
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
