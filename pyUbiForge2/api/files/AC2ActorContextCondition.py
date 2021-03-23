from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2ActorContextCondition(SubclassBaseFile):
    ResourceType = 0x5DB41292
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

