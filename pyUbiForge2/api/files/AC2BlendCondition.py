from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2BlendCondition(SubclassBaseFile):
    ResourceType = 0xF77741D9
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

