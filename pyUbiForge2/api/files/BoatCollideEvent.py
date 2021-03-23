from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class BoatCollideEvent(SubclassBaseFile):
    ResourceType = 0x1938687E
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
