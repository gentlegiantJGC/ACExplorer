from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlDoEvent import CannonControlDoEvent as _CannonControlDoEvent


class CannonControlDoAimEvent(SubclassBaseFile):
    ResourceType = 0x5C75BFD9
    ParentResourceType = _CannonControlDoEvent.ResourceType
    parent: _CannonControlDoEvent

