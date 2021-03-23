from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonDestroyedFinishedEvent(SubclassBaseFile):
    ResourceType = 0xA1196DAA
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent
