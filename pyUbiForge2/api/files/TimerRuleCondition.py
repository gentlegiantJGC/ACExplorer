from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class TimerRuleCondition(SubclassBaseFile):
    ResourceType = 0xC16C05E5
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

