from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class MountHorseEvent(SubclassBaseFile):
    ResourceType = 0x4A1A7994
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent

