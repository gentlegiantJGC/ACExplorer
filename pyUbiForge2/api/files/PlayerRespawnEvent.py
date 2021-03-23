from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerRespawnEvent(SubclassBaseFile):
    ResourceType = 0x073AD487
    ParentResourceType = _Event.ResourceType
    parent: _Event
