from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2MainTargetAssassinationCondition(SubclassBaseFile):
    ResourceType = 0x76CA8904
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
