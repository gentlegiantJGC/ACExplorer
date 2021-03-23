from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class TimedSwitchEventSeed_LGS(SubclassBaseFile):
    ResourceType = 0xA9DB545D
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
