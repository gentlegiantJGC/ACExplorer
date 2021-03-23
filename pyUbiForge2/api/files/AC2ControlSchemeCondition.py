from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2ControlSchemeCondition(SubclassBaseFile):
    ResourceType = 0x05BB887E
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
