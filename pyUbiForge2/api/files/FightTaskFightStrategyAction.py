from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyAction import FightStrategyAction as _FightStrategyAction


class FightTaskFightStrategyAction(SubclassBaseFile):
    ResourceType = 0xA6D39327
    ParentResourceType = _FightStrategyAction.ResourceType
    parent: _FightStrategyAction

