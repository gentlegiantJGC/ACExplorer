from pyUbiForge2.api.game import SubclassBaseFile
from .VehicleComponent import VehicleComponent as _VehicleComponent


class HorseHitchController(SubclassBaseFile):
    ResourceType = 0x3F25CE4E
    ParentResourceType = _VehicleComponent.ResourceType
    parent: _VehicleComponent
