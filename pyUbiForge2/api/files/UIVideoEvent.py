from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIVideoEvent(SubclassBaseFile):
    ResourceType = 0x7E02AFDB
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

