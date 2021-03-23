from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlEvent import CannonControlEvent as _CannonControlEvent


class CannonControlDoEvent(SubclassBaseFile):
    ResourceType = 0xE5617D06
    ParentResourceType = _CannonControlEvent.ResourceType
    parent: _CannonControlEvent

