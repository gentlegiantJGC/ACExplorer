from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerFleeingEvent(SubclassBaseFile):
    ResourceType = 0xB9225970
    ParentResourceType = _Event.ResourceType
    parent: _Event

