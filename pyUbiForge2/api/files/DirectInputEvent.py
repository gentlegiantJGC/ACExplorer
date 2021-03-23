from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DirectInputEvent(SubclassBaseFile):
    ResourceType = 0x63A2A7A1
    ParentResourceType = _Event.ResourceType
    parent: _Event
