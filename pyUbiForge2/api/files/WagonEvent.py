from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class WagonEvent(SubclassBaseFile):
    ResourceType = 0x5A39499A
    ParentResourceType = _Event.ResourceType
    parent: _Event

