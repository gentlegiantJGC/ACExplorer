from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class LockedByAssassinEvent(SubclassBaseFile):
    ResourceType = 0xDE8AC21C
    ParentResourceType = _Event.ResourceType
    parent: _Event

