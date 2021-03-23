from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2GroupTargetingCondition(SubclassBaseFile):
    ResourceType = 0x9A91C72F
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
