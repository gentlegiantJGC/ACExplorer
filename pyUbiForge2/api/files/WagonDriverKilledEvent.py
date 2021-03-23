from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonDriverKilledEvent(SubclassBaseFile):
    ResourceType = 0x52E50FC9
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent
