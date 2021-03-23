from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PrePauseEvent(SubclassBaseFile):
    ResourceType = 0x40445E58
    ParentResourceType = _Event.ResourceType
    parent: _Event
