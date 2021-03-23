from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class OddZoneEvent(SubclassBaseFile):
    ResourceType = 0x5069AD4E
    ParentResourceType = _Event.ResourceType
    parent: _Event

