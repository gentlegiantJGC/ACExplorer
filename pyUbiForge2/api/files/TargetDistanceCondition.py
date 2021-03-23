from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class TargetDistanceCondition(SubclassBaseFile):
    ResourceType = 0xAD7466F6
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
