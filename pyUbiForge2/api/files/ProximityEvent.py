from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ProximityEvent(SubclassBaseFile):
    ResourceType = 0x7502B30C
    ParentResourceType = _Event.ResourceType
    parent: _Event
