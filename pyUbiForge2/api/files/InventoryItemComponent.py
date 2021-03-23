from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class InventoryItemComponent(SubclassBaseFile):
    ResourceType = 0xE3D738DD
    ParentResourceType = _Component.ResourceType
    parent: _Component
