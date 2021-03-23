from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ComboKillResponseEvent(SubclassBaseFile):
    ResourceType = 0xBBF3B940
    ParentResourceType = _Event.ResourceType
    parent: _Event
