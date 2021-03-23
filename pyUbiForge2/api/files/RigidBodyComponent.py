from pyUbiForge2.api.game import SubclassBaseFile
from .InteractivePhysicComponent import (
    InteractivePhysicComponent as _InteractivePhysicComponent,
)


class RigidBodyComponent(SubclassBaseFile):
    ResourceType = 0xC177D702
    ParentResourceType = _InteractivePhysicComponent.ResourceType
    parent: _InteractivePhysicComponent
