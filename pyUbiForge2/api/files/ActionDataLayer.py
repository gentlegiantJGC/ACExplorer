from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionDataLayer(SubclassBaseFile):
    ResourceType = 0x30533CDC
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

