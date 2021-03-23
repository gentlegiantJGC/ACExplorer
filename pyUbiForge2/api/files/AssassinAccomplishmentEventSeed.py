from pyUbiForge2.api.game import SubclassBaseFile
from .SenderOverrideBroadcastingEventSeed import (
    SenderOverrideBroadcastingEventSeed as _SenderOverrideBroadcastingEventSeed,
)


class AssassinAccomplishmentEventSeed(SubclassBaseFile):
    ResourceType = 0xED892953
    ParentResourceType = _SenderOverrideBroadcastingEventSeed.ResourceType
    parent: _SenderOverrideBroadcastingEventSeed
