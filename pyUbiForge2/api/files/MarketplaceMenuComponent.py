from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class MarketplaceMenuComponent(SubclassBaseFile):
    ResourceType = 0xD8E1022A
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
