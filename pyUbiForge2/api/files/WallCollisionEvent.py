from pyUbiForge2.api.game import SubclassBaseFile
from .CollisionPerceptionEvent import (
    CollisionPerceptionEvent as _CollisionPerceptionEvent,
)


class WallCollisionEvent(SubclassBaseFile):
    ResourceType = 0xA33429C5
    ParentResourceType = _CollisionPerceptionEvent.ResourceType
    parent: _CollisionPerceptionEvent
