from pyUbiForge2.api.game import SubclassBaseFile
from .LoadingEvent import LoadingEvent as _LoadingEvent


class StartLoadingEvent(SubclassBaseFile):
    ResourceType = 0xA5C210C2
    ParentResourceType = _LoadingEvent.ResourceType
    parent: _LoadingEvent
