from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class BooleanRuleCondition(SubclassBaseFile):
    ResourceType = 0xB133A7EA
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
