from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2JumpHeightCondition(SubclassBaseFile):
    ResourceType = 0x7DCDBEFF
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

