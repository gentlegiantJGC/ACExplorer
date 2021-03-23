from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class ShopsMenu(SubclassBaseFile):
    ResourceType = 0x9A053370
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

