from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class MarketingCameraCondition(SubclassBaseFile):
    ResourceType = 0xD57A1B06
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
