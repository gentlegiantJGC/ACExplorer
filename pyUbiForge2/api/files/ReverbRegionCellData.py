from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class ReverbRegionCellData(SubclassBaseFile):
    ResourceType = 0xD0483E1F
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData

