from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ADBLetterEvent(SubclassBaseFile):
    ResourceType = 0x6181E98B
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

