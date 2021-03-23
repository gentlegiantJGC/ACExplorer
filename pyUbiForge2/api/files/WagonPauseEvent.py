from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonPauseEvent(SubclassBaseFile):
    ResourceType = 0x57351E6B
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent
