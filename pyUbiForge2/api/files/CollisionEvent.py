from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CollisionEvent(SubclassBaseFile):
    ResourceType = 0xEA436A52
    ParentResourceType = _Event.ResourceType
    parent: _Event
