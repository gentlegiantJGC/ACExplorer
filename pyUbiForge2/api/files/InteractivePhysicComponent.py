from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class InteractivePhysicComponent(SubclassBaseFile):
    ResourceType = 0x138F82BB
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent

