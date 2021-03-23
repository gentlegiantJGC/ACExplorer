from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TeleportEvent(SubclassBaseFile):
    ResourceType = 0x35D7E61F
    ParentResourceType = _Event.ResourceType
    parent: _Event

