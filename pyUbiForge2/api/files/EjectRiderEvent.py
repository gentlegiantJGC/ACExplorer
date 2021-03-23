from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class EjectRiderEvent(SubclassBaseFile):
    ResourceType = 0xC807B79A
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent

