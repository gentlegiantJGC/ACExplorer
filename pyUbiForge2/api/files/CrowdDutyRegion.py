from pyUbiForge2.api.game import SubclassBaseFile
from .CrowdRegion import CrowdRegion as _CrowdRegion


class CrowdDutyRegion(SubclassBaseFile):
    ResourceType = 0x5B8B9990
    ParentResourceType = _CrowdRegion.ResourceType
    parent: _CrowdRegion

