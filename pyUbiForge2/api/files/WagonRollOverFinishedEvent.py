from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonRollOverFinishedEvent(SubclassBaseFile):
    ResourceType = 0x88925BBC
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent
