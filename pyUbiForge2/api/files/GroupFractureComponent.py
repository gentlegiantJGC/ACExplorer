from pyUbiForge2.api.game import SubclassBaseFile
from .InteractivePhysicComponent import (
    InteractivePhysicComponent as _InteractivePhysicComponent,
)


class GroupFractureComponent(SubclassBaseFile):
    ResourceType = 0xC4EF6CF2
    ParentResourceType = _InteractivePhysicComponent.ResourceType
    parent: _InteractivePhysicComponent
