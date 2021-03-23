from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GrabResponseEvent(SubclassBaseFile):
    ResourceType = 0xA83BC4B6
    ParentResourceType = _Event.ResourceType
    parent: _Event
