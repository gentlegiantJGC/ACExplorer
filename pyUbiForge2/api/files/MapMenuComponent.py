from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class MapMenuComponent(SubclassBaseFile):
    ResourceType = 0xAFB1FCCD
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
