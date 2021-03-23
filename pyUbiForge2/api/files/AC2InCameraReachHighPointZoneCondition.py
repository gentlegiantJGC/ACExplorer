from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2InCameraReachHighPointZoneCondition(SubclassBaseFile):
    ResourceType = 0xD2E35954
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition
