from pyUbiForge2.api.game import SubclassBaseFile
from .HorseEvent import HorseEvent as _HorseEvent


class EnableCruiseControlEvent(SubclassBaseFile):
    ResourceType = 0x3E20AF85
    ParentResourceType = _HorseEvent.ResourceType
    parent: _HorseEvent
