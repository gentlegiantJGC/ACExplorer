from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class WorldAmbianceEvent(SubclassBaseFile):
    ResourceType = 0xCEFFEF0F
    ParentResourceType = _Event.ResourceType
    parent: _Event

