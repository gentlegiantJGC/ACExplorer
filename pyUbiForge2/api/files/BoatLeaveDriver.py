from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class BoatLeaveDriver(SubclassBaseFile):
    ResourceType = 0x2FF3B966
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent

