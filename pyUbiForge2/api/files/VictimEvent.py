from pyUbiForge2.api.game import SubclassBaseFile
from .DangerEvent import DangerEvent as _DangerEvent


class VictimEvent(SubclassBaseFile):
    ResourceType = 0x3D732C8A
    ParentResourceType = _DangerEvent.ResourceType
    parent: _DangerEvent

