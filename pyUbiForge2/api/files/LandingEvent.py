from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class LandingEvent(SubclassBaseFile):
    ResourceType = 0x88A81931
    ParentResourceType = _Event.ResourceType
    parent: _Event
