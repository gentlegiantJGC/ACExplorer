from pyUbiForge2.api.game import SubclassBaseFile
from .CollisionPerceptionEvent import (
    CollisionPerceptionEvent as _CollisionPerceptionEvent,
)


class EntityCollisionEvent(SubclassBaseFile):
    ResourceType = 0x53103497
    ParentResourceType = _CollisionPerceptionEvent.ResourceType
    parent: _CollisionPerceptionEvent
