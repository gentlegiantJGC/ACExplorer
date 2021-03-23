from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class StepAttackFightStrategyAction(SubclassBaseFile):
    ResourceType = 0xF7F0BF9C
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction

