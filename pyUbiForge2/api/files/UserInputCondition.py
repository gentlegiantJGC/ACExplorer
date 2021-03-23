from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class UserInputCondition(SubclassBaseFile):
    ResourceType = 0x5B6AB63F
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
