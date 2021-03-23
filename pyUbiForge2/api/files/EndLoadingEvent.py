from pyUbiForge2.api.game import SubclassBaseFile
from .LoadingEvent import LoadingEvent as _LoadingEvent


class EndLoadingEvent(SubclassBaseFile):
    ResourceType = 0x53DDEA6D
    ParentResourceType = _LoadingEvent.ResourceType
    parent: _LoadingEvent

