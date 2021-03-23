from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class EjectFromBoatEvent(SubclassBaseFile):
    ResourceType = 0xD181EA45
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
