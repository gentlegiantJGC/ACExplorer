from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerVanishingEvent(SubclassBaseFile):
    ResourceType = 0x90F5FD5E
    ParentResourceType = _Event.ResourceType
    parent: _Event

