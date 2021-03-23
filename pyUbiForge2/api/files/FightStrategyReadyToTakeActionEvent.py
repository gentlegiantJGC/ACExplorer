from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyReadyToTakeActionEvent(SubclassBaseFile):
    ResourceType = 0x4F67E055
    ParentResourceType = _Event.ResourceType
    parent: _Event

