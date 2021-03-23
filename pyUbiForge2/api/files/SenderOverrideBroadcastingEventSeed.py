from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class SenderOverrideBroadcastingEventSeed(SubclassBaseFile):
    ResourceType = 0x7519B348
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

