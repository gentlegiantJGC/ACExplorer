from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CameraEvent(SubclassBaseFile):
    ResourceType = 0xAB3DA623
    ParentResourceType = _Event.ResourceType
    parent: _Event
