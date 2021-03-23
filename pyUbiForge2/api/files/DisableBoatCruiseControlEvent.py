from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class DisableBoatCruiseControlEvent(SubclassBaseFile):
    ResourceType = 0x94082513
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
