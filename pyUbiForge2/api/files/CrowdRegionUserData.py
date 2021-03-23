from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellUserData import RegionCellUserData as _RegionCellUserData


class CrowdRegionUserData(SubclassBaseFile):
    ResourceType = 0x861F848D
    ParentResourceType = _RegionCellUserData.ResourceType
    parent: _RegionCellUserData

