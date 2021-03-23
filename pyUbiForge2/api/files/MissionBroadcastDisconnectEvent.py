from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionBroadcastDisconnectEvent(SubclassBaseFile):
    ResourceType = 0xE74A09CC
    ParentResourceType = _Event.ResourceType
    parent: _Event
