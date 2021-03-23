from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class ConditionPatternRuleCondition(SubclassBaseFile):
    ResourceType = 0x0294E135
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

