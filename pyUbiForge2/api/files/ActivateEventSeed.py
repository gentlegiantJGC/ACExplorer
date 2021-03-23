from pyUbiForge2.api.game import SubclassBaseFile
from .SenderOverrideBroadcastingEventSeed import (
    SenderOverrideBroadcastingEventSeed as _SenderOverrideBroadcastingEventSeed,
)


class ActivateEventSeed(SubclassBaseFile):
    ResourceType = 0xA117C2BE
    ParentResourceType = _SenderOverrideBroadcastingEventSeed.ResourceType
    parent: _SenderOverrideBroadcastingEventSeed
