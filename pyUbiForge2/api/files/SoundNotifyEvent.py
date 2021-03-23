from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SoundNotifyEvent(SubclassBaseFile):
    ResourceType = 0x942E5E39
    ParentResourceType = _Event.ResourceType
    parent: _Event
