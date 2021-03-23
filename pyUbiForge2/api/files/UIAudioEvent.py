from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIAudioEvent(SubclassBaseFile):
    ResourceType = 0x3624EE5B
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

