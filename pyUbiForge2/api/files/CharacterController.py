from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class CharacterController(SubclassBaseFile):
    ResourceType = 0xEFE71078
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent
