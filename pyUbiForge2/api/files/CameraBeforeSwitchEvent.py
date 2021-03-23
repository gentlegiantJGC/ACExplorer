from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CameraBeforeSwitchEvent(SubclassBaseFile):
    ResourceType = 0xCAF29798
    ParentResourceType = _Event.ResourceType
    parent: _Event
