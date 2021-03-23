from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionAFSMessage(SubclassBaseFile):
    ResourceType = 0xFE1A95A0
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
