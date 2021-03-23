from pyUbiForge2.api.game import SubclassBaseFile
from .BoatEvent import BoatEvent as _BoatEvent


class BoatEnterDriver(SubclassBaseFile):
    ResourceType = 0x1A44EFA2
    ParentResourceType = _BoatEvent.ResourceType
    parent: _BoatEvent

