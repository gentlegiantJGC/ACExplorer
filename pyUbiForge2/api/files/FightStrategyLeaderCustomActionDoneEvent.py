from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyLeaderCustomActionDoneEvent(SubclassBaseFile):
    ResourceType = 0xCF1BAF70
    ParentResourceType = _Event.ResourceType
    parent: _Event
