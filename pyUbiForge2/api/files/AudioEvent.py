from pyUbiForge2.api.game import SubclassBaseFile
from .AudioBaseEvent import AudioBaseEvent as _AudioBaseEvent


class AudioEvent(SubclassBaseFile):
    ResourceType = 0xA7A64A34
    ParentResourceType = _AudioBaseEvent.ResourceType
    parent: _AudioBaseEvent
