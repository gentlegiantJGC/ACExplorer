from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2FightCondition(SubclassBaseFile):
    ResourceType = 0xD0D4A8E5
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
