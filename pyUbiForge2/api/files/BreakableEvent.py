from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BreakableEvent(SubclassBaseFile):
    ResourceType = 0x52DC76D4
    ParentResourceType = _Event.ResourceType
    parent: _Event

