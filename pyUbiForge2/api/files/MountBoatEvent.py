from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class MountBoatEvent(SubclassBaseFile):
    ResourceType = 0x3702DC90
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent
