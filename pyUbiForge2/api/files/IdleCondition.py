from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class IdleCondition(SubclassBaseFile):
    ResourceType = 0xAA165F33
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

