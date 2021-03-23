from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class SetEquipmentHudModeEvent(SubclassBaseFile):
    ResourceType = 0x4784599C
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
