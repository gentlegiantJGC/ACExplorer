from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2OutOfBoundsCondition(SubclassBaseFile):
    ResourceType = 0xE1E12604
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
