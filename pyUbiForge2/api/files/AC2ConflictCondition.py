from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2ConflictCondition(SubclassBaseFile):
    ResourceType = 0x6B08569A
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

