from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2AssassinationTypeCondition(SubclassBaseFile):
    ResourceType = 0x0BE2132D
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
