from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2SecondaryTargetCondition(SubclassBaseFile):
    ResourceType = 0xCBF5BD29
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

