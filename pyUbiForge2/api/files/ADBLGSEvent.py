from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ADBLGSEvent(SubclassBaseFile):
    ResourceType = 0x52BDCF2A
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

