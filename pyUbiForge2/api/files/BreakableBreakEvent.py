from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BreakableBreakEvent(SubclassBaseFile):
    ResourceType = 0x7FA87A2A
    ParentResourceType = _Event.ResourceType
    parent: _Event

