from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightManagerPlayerEvent(SubclassBaseFile):
    ResourceType = 0xDA38765E
    ParentResourceType = _Event.ResourceType
    parent: _Event

