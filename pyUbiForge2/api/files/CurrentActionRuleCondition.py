from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class CurrentActionRuleCondition(SubclassBaseFile):
    ResourceType = 0x6D8397B0
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
