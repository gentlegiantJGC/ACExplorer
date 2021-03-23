from pyUbiForge2.api.game import SubclassBaseFile
from .SenderOverrideBroadcastingEventSeed import SenderOverrideBroadcastingEventSeed as _SenderOverrideBroadcastingEventSeed


class PulseTriggerEventSeed(SubclassBaseFile):
    ResourceType = 0x850CC6B7
    ParentResourceType = _SenderOverrideBroadcastingEventSeed.ResourceType
    parent: _SenderOverrideBroadcastingEventSeed

