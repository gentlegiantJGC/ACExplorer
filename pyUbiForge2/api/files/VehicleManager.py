from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class VehicleManager(SubclassBaseFile):
    ResourceType = 0xA81082AD
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
