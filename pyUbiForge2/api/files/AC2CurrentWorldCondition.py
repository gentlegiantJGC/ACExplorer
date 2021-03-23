from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2CurrentWorldCondition(SubclassBaseFile):
    ResourceType = 0x392EC803
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
