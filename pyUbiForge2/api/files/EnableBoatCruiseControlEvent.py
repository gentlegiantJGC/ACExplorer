from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class EnableBoatCruiseControlEvent(SubclassBaseFile):
    ResourceType = 0x900F793D
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent

