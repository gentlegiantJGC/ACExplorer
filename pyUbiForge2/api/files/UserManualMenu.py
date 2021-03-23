from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class UserManualMenu(SubclassBaseFile):
    ResourceType = 0x5BE664A7
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

