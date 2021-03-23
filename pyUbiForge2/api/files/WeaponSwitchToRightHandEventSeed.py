from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WeaponSwitchToRightHandEventSeed(SubclassBaseFile):
    ResourceType = 0x4C09BEBD
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

