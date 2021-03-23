from pyUbiForge2.api.game import SubclassBaseFile
from .SenderOverrideBroadcastingEventSeed import SenderOverrideBroadcastingEventSeed as _SenderOverrideBroadcastingEventSeed


class OddZoneEventSeed(SubclassBaseFile):
    ResourceType = 0x918A2C1F
    ParentResourceType = _SenderOverrideBroadcastingEventSeed.ResourceType
    parent: _SenderOverrideBroadcastingEventSeed

