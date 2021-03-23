from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class TargetSpeedCondition(SubclassBaseFile):
    ResourceType = 0x095553B7
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

