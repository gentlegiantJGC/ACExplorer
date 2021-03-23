from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class DisableCruiseControlEvent(SubclassBaseFile):
    ResourceType = 0xEB87689E
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
