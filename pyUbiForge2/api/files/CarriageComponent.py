from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleComponent import VehicleComponent as _VehicleComponent


class CarriageComponent(SubclassBaseFile):
    ResourceType = 0xAC77440A
    ParentResourceType = _VehicleComponent.ResourceType
    parent: _VehicleComponent
