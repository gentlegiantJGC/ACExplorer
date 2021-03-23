from pyUbiForge2.api.game import SubclassBaseFile
from .AudioBaseEvent import AudioBaseEvent as _AudioBaseEvent


class SpeechEvent(SubclassBaseFile):
    ResourceType = 0x90D9EC94
    ParentResourceType = _AudioBaseEvent.ResourceType
    parent: _AudioBaseEvent

