from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2DropBodyCondition(SubclassBaseFile):
    ResourceType = 0xF91C86B2
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

