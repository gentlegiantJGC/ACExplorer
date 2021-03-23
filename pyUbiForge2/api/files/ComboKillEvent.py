from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ComboKillEvent(SubclassBaseFile):
    ResourceType = 0xB454191B
    ParentResourceType = _Event.ResourceType
    parent: _Event

