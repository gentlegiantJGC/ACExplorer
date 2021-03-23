from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TauntPlayerEvent(SubclassBaseFile):
    ResourceType = 0x5EC8DB40
    ParentResourceType = _Event.ResourceType
    parent: _Event

