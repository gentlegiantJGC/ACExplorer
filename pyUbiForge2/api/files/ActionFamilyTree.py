from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionFamilyTree(SubclassBaseFile):
    ResourceType = 0x2DEF9C36
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
