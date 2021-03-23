from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class RagdollComponent(SubclassBaseFile):
    ResourceType = 0x9908895A
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent
