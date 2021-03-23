from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FastTravelMenuEvent(SubclassBaseFile):
    ResourceType = 0xC86F0685
    ParentResourceType = _Event.ResourceType
    parent: _Event
