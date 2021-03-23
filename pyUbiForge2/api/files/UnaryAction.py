from pyUbiForge2.api.game import SubclassBaseFile
from .PhysicsAction import PhysicsAction as _PhysicsAction


class UnaryAction(SubclassBaseFile):
    ResourceType = 0x807F4ABC
    ParentResourceType = _PhysicsAction.ResourceType
    parent: _PhysicsAction

