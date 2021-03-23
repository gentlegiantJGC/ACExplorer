from pyUbiForge2.api.game import SubclassBaseFile
from .UIInventoryInfo import UIInventoryInfo as _UIInventoryInfo


class UIInventoryItem(SubclassBaseFile):
    ResourceType = 0xB200A026
    ParentResourceType = _UIInventoryInfo.ResourceType
    parent: _UIInventoryInfo

