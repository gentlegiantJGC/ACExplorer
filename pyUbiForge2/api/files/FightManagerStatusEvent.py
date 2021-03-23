from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightManagerStatusEvent(SubclassBaseFile):
    ResourceType = 0x40248BF9
    ParentResourceType = _Event.ResourceType
    parent: _Event

