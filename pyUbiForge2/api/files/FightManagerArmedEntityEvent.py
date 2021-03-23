from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightManagerArmedEntityEvent(SubclassBaseFile):
    ResourceType = 0xAC81938D
    ParentResourceType = _Event.ResourceType
    parent: _Event

