from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class WalkthroughGPUCondition(SubclassBaseFile):
    ResourceType = 0x487E1EB6
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
