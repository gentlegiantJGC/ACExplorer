from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class DismountBoatEvent(SubclassBaseFile):
    ResourceType = 0x3F675D85
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent

