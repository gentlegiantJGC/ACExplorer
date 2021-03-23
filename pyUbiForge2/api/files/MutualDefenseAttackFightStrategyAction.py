from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class MutualDefenseAttackFightStrategyAction(SubclassBaseFile):
    ResourceType = 0xCAE03EBC
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction

