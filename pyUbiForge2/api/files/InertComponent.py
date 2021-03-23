from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class InertComponent(SubclassBaseFile):
    ResourceType = 0x0E5A450A
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent
