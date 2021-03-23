from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class VillaInventoryItemComponent(SubclassBaseFile):
    ResourceType = 0xCBD98F8B
    ParentResourceType = _Component.ResourceType
    parent: _Component
