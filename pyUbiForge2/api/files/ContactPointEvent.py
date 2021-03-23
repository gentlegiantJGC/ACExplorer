from pyUbiForge2.api.game import SubclassBaseFile
from .CollisionEvent import CollisionEvent as _CollisionEvent


class ContactPointEvent(SubclassBaseFile):
    ResourceType = 0x6C590196
    ParentResourceType = _CollisionEvent.ResourceType
    parent: _CollisionEvent
