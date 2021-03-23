from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class StatsMenu(SubclassBaseFile):
    ResourceType = 0x7ABF2E5F
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
