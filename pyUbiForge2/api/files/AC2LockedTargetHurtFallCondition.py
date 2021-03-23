from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2LockedTargetHurtFallCondition(SubclassBaseFile):
    ResourceType = 0x71C54D9C
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

