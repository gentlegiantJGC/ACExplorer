from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class HighProfileCondition(SubclassBaseFile):
    ResourceType = 0x92202E75
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
