from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleComponent import VehicleComponent as _VehicleComponent


class WagonController(SubclassBaseFile):
    ResourceType = 0x185819ED
    ParentResourceType = _VehicleComponent.ResourceType
    parent: _VehicleComponent
