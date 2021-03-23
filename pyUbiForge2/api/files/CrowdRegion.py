from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class CrowdRegion(SubclassBaseFile):
    ResourceType = 0x352B704E
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData

