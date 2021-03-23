from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class InventoryCondition(SubclassBaseFile):
    ResourceType = 0xF8EB4D21
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

