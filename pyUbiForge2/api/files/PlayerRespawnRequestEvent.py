from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerRespawnRequestEvent(SubclassBaseFile):
    ResourceType = 0xA11FF048
    ParentResourceType = _Event.ResourceType
    parent: _Event

