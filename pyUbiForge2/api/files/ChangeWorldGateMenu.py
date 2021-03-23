from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class ChangeWorldGateMenu(SubclassBaseFile):
    ResourceType = 0x89A3E5A4
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

