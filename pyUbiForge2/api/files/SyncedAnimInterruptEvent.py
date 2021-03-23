from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SyncedAnimInterruptEvent(SubclassBaseFile):
    ResourceType = 0x802FA345
    ParentResourceType = _Event.ResourceType
    parent: _Event
