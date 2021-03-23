from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerDeathEvent(SubclassBaseFile):
    ResourceType = 0x440CEF8A
    ParentResourceType = _Event.ResourceType
    parent: _Event

