from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2EventCondition(SubclassBaseFile):
    ResourceType = 0x3B4CAA0D
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

