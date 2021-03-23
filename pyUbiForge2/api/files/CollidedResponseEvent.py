from pyUbiForge2.api.game import SubclassBaseFile
from .CollidedEvent import CollidedEvent as _CollidedEvent


class CollidedResponseEvent(SubclassBaseFile):
    ResourceType = 0xF758C6F2
    ParentResourceType = _CollidedEvent.ResourceType
    parent: _CollidedEvent

