from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DefenseBreakEvent(SubclassBaseFile):
    ResourceType = 0xE86734D0
    ParentResourceType = _Event.ResourceType
    parent: _Event

