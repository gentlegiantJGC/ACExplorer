from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class CapeEquipMenuEnableAction(SubclassBaseFile):
    ResourceType = 0x20D010F3
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

