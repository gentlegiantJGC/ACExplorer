from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class HorseStateChangeEvent(SubclassBaseFile):
    ResourceType = 0xF40AD66B
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
