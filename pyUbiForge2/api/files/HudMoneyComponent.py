from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class HudMoneyComponent(SubclassBaseFile):
    ResourceType = 0x07BE01FD
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
