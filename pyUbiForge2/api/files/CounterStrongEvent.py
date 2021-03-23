from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CounterStrongEvent(SubclassBaseFile):
    ResourceType = 0x2B237696
    ParentResourceType = _Event.ResourceType
    parent: _Event

