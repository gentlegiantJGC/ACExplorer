from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class HorseEvent(SubclassBaseFile):
    ResourceType = 0xBABC715B
    ParentResourceType = _Event.ResourceType
    parent: _Event

