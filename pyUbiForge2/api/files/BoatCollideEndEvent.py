from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class BoatCollideEndEvent(SubclassBaseFile):
    ResourceType = 0x4577E835
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
