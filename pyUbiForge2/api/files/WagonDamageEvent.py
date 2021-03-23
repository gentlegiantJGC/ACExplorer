from pyUbiForge2.api.game import SubclassBaseFile
from .WagonEvent import WagonEvent as _WagonEvent


class WagonDamageEvent(SubclassBaseFile):
    ResourceType = 0xE0928D12
    ParentResourceType = _WagonEvent.ResourceType
    parent: _WagonEvent

