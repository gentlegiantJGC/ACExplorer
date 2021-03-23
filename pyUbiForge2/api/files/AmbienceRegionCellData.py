from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class AmbienceRegionCellData(SubclassBaseFile):
    ResourceType = 0xD9386B33
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData
