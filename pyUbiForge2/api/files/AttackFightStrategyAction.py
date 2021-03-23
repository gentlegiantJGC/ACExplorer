from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class AttackFightStrategyAction(SubclassBaseFile):
    ResourceType = 0xF6886C9E
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction
