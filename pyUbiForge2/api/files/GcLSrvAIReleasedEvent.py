from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GcLSrvAIReleasedEvent(SubclassBaseFile):
    ResourceType = 0x84103F00
    ParentResourceType = _Event.ResourceType
    parent: _Event

