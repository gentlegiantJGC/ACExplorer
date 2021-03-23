from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlDoEvent import CannonControlDoEvent as _CannonControlDoEvent


class CannonControlDoFireEvent(SubclassBaseFile):
    ResourceType = 0x9037EEA2
    ParentResourceType = _CannonControlDoEvent.ResourceType
    parent: _CannonControlDoEvent

