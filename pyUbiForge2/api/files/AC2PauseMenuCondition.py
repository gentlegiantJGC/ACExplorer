from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2PauseMenuCondition(SubclassBaseFile):
    ResourceType = 0xAAAD251D
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
