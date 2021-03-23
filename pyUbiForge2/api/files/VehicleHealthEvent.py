from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleEvent import VehicleEvent as _VehicleEvent


class VehicleHealthEvent(SubclassBaseFile):
    ResourceType = 0x87CCCA05
    ParentResourceType = _VehicleEvent.ResourceType
    parent: _VehicleEvent
