from pyUbiForge2.api.game import SubclassBaseFile
from .CollidedEvent import CollidedEvent as _CollidedEvent


class CollidedRequestEvent(SubclassBaseFile):
    ResourceType = 0x07DB36CA
    ParentResourceType = _CollidedEvent.ResourceType
    parent: _CollidedEvent
