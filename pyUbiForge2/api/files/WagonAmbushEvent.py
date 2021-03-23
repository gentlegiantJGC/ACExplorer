from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonAmbushEvent(SubclassBaseFile):
    ResourceType = 0x83BE9ADD
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent

