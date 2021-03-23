from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2ChargeLevelAttackCondition(SubclassBaseFile):
    ResourceType = 0x3937D81E
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

