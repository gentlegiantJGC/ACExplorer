from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlDoEvent import CannonControlDoEvent as _CannonControlDoEvent


class CannonControlDoReloadEvent(SubclassBaseFile):
    ResourceType = 0xFBF99510
    ParentResourceType = _CannonControlDoEvent.ResourceType
    parent: _CannonControlDoEvent
