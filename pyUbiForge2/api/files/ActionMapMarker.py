from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionMapMarker(SubclassBaseFile):
    ResourceType = 0x7C8E0F03
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
