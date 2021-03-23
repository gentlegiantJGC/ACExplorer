from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlDoEvent import CannonControlDoEvent as _CannonControlDoEvent


class CannonControlDoLeaveEvent(SubclassBaseFile):
    ResourceType = 0xF7CF56EF
    ParentResourceType = _CannonControlDoEvent.ResourceType
    parent: _CannonControlDoEvent
