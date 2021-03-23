from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class FamilyTreeMenu(SubclassBaseFile):
    ResourceType = 0xEE19822B
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
