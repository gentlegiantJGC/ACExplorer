from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyPerformCustomActionEvent(SubclassBaseFile):
    ResourceType = 0x8FB5BF69
    ParentResourceType = _Event.ResourceType
    parent: _Event
