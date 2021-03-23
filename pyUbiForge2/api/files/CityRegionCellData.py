from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class CityRegionCellData(SubclassBaseFile):
    ResourceType = 0x3970BD2D
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData
