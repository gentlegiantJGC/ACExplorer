from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class LoadingEvent(SubclassBaseFile):
    ResourceType = 0x8FAB8072
    ParentResourceType = _Event.ResourceType
    parent: _Event
