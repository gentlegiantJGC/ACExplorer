from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class AmbienceEventSeed(SubclassBaseFile):
    ResourceType = 0x1B99FB85
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

