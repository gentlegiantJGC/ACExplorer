from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyAbortEvent(SubclassBaseFile):
    ResourceType = 0xA98E62F3
    ParentResourceType = _Event.ResourceType
    parent: _Event
