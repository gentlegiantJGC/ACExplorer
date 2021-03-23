from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class DropObjectEventSeed(SubclassBaseFile):
    ResourceType = 0x4535876F
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

