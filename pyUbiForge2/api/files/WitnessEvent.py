from pyUbiForge2.api.game import SubclassBaseFile
from .DangerEvent import DangerEvent as _DangerEvent


class WitnessEvent(SubclassBaseFile):
    ResourceType = 0x40E3EABD
    ParentResourceType = _DangerEvent.ResourceType
    parent: _DangerEvent

