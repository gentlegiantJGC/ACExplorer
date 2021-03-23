from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2DesynchronizationCondition(SubclassBaseFile):
    ResourceType = 0x15F098EC
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
