from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2PlayerGroundHeightCondition(SubclassBaseFile):
    ResourceType = 0x4444AF59
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

