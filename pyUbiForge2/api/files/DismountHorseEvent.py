from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class DismountHorseEvent(SubclassBaseFile):
    ResourceType = 0x27CFF8FE
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
