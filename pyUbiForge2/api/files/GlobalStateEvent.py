from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class GlobalStateEvent(SubclassBaseFile):
    ResourceType = 0xFA566E57
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
