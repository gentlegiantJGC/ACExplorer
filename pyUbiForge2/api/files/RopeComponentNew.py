from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicComponent import PhysicComponent as _PhysicComponent


class RopeComponentNew(SubclassBaseFile):
    ResourceType = 0xF8E78FD9
    ParentResourceType = _PhysicComponent.ResourceType
    parent: _PhysicComponent

