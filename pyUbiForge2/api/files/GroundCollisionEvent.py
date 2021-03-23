from pyUbiForge2.api.game import SubclassBaseFile
from .CollisionPerceptionEvent import CollisionPerceptionEvent as _CollisionPerceptionEvent


class GroundCollisionEvent(SubclassBaseFile):
    ResourceType = 0x19595AFE
    ParentResourceType = _CollisionPerceptionEvent.ResourceType
    parent: _CollisionPerceptionEvent

