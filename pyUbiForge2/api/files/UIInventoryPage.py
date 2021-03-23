from pyUbiForge2.api.game import SubclassBaseFile
from .UIInventoryInfo import UIInventoryInfo as _UIInventoryInfo


class UIInventoryPage(SubclassBaseFile):
    ResourceType = 0xB9113318
    ParentResourceType = _UIInventoryInfo.ResourceType
    parent: _UIInventoryInfo
