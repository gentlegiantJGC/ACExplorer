from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class UpdateDrivingAnimationsEvent(SubclassBaseFile):
    ResourceType = 0x5BD9C34C
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent

