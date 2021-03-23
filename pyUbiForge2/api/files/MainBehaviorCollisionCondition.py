from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class MainBehaviorCollisionCondition(SubclassBaseFile):
    ResourceType = 0x2D2240BC
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

