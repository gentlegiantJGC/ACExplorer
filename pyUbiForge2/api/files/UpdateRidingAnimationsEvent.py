from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class UpdateRidingAnimationsEvent(SubclassBaseFile):
    ResourceType = 0xBF854EEF
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
