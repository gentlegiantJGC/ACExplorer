from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionPlayerHealth(SubclassBaseFile):
    ResourceType = 0x9C24E90D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

