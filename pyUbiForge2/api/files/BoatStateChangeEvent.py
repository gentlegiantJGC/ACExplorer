from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class BoatStateChangeEvent(SubclassBaseFile):
    ResourceType = 0x588C54DC
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
