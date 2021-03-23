from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SyncedAnimEndEvent(SubclassBaseFile):
    ResourceType = 0xAC631AE8
    ParentResourceType = _Event.ResourceType
    parent: _Event

