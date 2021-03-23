from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleComponent import VehicleComponent as _VehicleComponent


class BoatController(SubclassBaseFile):
    ResourceType = 0x45C649DA
    ParentResourceType = _VehicleComponent.ResourceType
    parent: _VehicleComponent

