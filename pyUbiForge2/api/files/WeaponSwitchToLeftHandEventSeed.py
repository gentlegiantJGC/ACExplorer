from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WeaponSwitchToLeftHandEventSeed(SubclassBaseFile):
    ResourceType = 0x15C383A5
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
