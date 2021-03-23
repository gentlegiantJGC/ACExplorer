from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonDisembarkEvent(SubclassBaseFile):
    ResourceType = 0x4114DC19
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent

