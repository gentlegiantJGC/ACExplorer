from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class UniqueEventObjectEvent(SubclassBaseFile):
    ResourceType = 0x9E50C696
    ParentResourceType = _Event.ResourceType
    parent: _Event
