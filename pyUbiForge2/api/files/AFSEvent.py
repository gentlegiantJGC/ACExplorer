from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class AFSEvent(SubclassBaseFile):
    ResourceType = 0x1199F5BE
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

