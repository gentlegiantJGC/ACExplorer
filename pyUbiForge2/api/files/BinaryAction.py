from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicsAction import PhysicsAction as _PhysicsAction


class BinaryAction(SubclassBaseFile):
    ResourceType = 0x6E05CD8B
    ParentResourceType = _PhysicsAction.ResourceType
    parent: _PhysicsAction

