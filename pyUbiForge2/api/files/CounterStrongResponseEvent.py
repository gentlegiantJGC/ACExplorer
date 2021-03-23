from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CounterStrongResponseEvent(SubclassBaseFile):
    ResourceType = 0x4B4298FF
    ParentResourceType = _Event.ResourceType
    parent: _Event

