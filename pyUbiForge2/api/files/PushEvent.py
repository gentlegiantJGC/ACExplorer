from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PushEvent(SubclassBaseFile):
    ResourceType = 0x6A50E579
    ParentResourceType = _Event.ResourceType
    parent: _Event
