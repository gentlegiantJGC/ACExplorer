from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyPerformActionEvent(SubclassBaseFile):
    ResourceType = 0xDE929C02
    ParentResourceType = _Event.ResourceType
    parent: _Event
