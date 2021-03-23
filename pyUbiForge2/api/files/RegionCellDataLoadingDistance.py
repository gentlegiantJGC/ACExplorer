from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class RegionCellDataLoadingDistance(SubclassBaseFile):
    ResourceType = 0x084850E3
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData

