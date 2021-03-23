from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class MultiInertComponent(SubclassBaseFile):
    ResourceType = 0x8BBEEE57
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent

