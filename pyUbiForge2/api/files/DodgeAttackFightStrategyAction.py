from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class DodgeAttackFightStrategyAction(SubclassBaseFile):
    ResourceType = 0x1DE48438
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction

