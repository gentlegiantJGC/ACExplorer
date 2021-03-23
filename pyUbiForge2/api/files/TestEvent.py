from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TestEvent(SubclassBaseFile):
    ResourceType = 0x20C2FDD4
    ParentResourceType = _Event.ResourceType
    parent: _Event

