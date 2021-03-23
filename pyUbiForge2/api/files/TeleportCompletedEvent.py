from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TeleportCompletedEvent(SubclassBaseFile):
    ResourceType = 0xA7F106A7
    ParentResourceType = _Event.ResourceType
    parent: _Event
