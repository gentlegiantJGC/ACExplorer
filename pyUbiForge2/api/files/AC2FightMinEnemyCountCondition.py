from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2FightMinEnemyCountCondition(SubclassBaseFile):
    ResourceType = 0xE6EC7BBA
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

