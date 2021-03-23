from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class CitySectorRegionCellData(SubclassBaseFile):
    ResourceType = 0x2FDFAF12
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData
