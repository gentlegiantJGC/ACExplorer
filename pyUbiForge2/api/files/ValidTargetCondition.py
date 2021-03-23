from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class ValidTargetCondition(SubclassBaseFile):
    ResourceType = 0x72ED1616
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

