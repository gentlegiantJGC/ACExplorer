from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryWorldComponent import MandatoryWorldComponent as _MandatoryWorldComponent


class RentAVehicleWorldComponent(SubclassBaseFile):
    ResourceType = 0x1340BB05
    ParentResourceType = _MandatoryWorldComponent.ResourceType
    parent: _MandatoryWorldComponent

