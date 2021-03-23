from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class HorseForgetRiderEvent(SubclassBaseFile):
    ResourceType = 0x3C280E45
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
