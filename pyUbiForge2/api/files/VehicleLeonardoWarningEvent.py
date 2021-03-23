from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleEvent import VehicleEvent as _VehicleEvent


class VehicleLeonardoWarningEvent(SubclassBaseFile):
    ResourceType = 0xDF229183
    ParentResourceType = _VehicleEvent.ResourceType
    parent: _VehicleEvent
