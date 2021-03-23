from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyActionDoneEvent(SubclassBaseFile):
    ResourceType = 0xD5596B3C
    ParentResourceType = _Event.ResourceType
    parent: _Event

