from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class GroupPhysicZone(SubclassBaseFile):
    ResourceType = 0x06A4ADC7
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent

