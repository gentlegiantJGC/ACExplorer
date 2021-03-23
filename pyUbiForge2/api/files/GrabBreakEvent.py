from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GrabBreakEvent(SubclassBaseFile):
    ResourceType = 0xC6F388BD
    ParentResourceType = _Event.ResourceType
    parent: _Event

