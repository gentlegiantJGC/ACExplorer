from pyUbiForge2.api.game import SubclassBaseFile
from .SenderOverrideBroadcastingEventSeed import SenderOverrideBroadcastingEventSeed as _SenderOverrideBroadcastingEventSeed


class FXEventSeed(SubclassBaseFile):
    ResourceType = 0x2350A2E0
    ParentResourceType = _SenderOverrideBroadcastingEventSeed.ResourceType
    parent: _SenderOverrideBroadcastingEventSeed

