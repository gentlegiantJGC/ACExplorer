from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2HangTypeCondition(SubclassBaseFile):
    ResourceType = 0xCD15CEFF
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
