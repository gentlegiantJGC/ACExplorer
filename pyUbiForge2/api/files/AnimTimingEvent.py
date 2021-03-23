from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AnimTimingEvent(SubclassBaseFile):
    ResourceType = 0xA9264210
    ParentResourceType = _Event.ResourceType
    parent: _Event
