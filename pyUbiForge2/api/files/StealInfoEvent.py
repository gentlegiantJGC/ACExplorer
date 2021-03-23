from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class StealInfoEvent(SubclassBaseFile):
    ResourceType = 0x803526B6
    ParentResourceType = _Event.ResourceType
    parent: _Event
