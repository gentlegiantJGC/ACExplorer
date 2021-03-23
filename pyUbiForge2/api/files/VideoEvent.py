from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VideoEvent(SubclassBaseFile):
    ResourceType = 0xEF800BB4
    ParentResourceType = _Event.ResourceType
    parent: _Event
