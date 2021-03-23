from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonClearAmbusherEvent(SubclassBaseFile):
    ResourceType = 0x51E1225F
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent
