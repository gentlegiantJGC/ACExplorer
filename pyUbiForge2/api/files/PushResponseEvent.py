from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PushResponseEvent(SubclassBaseFile):
    ResourceType = 0x27B7CD05
    ParentResourceType = _Event.ResourceType
    parent: _Event
