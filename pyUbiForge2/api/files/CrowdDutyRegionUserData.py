from pyUbiForge2.api.game import SubclassBaseFile
from .CrowdRegionUserData import CrowdRegionUserData as _CrowdRegionUserData


class CrowdDutyRegionUserData(SubclassBaseFile):
    ResourceType = 0x3CAEDBA5
    ParentResourceType = _CrowdRegionUserData.ResourceType
    parent: _CrowdRegionUserData

