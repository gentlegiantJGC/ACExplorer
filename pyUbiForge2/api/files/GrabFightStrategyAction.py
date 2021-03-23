from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class GrabFightStrategyAction(SubclassBaseFile):
    ResourceType = 0x44A3106E
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction

