from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DefenseBreakResponseEvent(SubclassBaseFile):
    ResourceType = 0x4D58EDB4
    ParentResourceType = _Event.ResourceType
    parent: _Event

