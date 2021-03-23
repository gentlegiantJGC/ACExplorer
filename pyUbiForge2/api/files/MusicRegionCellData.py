from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class MusicRegionCellData(SubclassBaseFile):
    ResourceType = 0x6AA4470F
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData
