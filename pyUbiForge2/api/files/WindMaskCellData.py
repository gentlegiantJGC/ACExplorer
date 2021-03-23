from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class WindMaskCellData(SubclassBaseFile):
    ResourceType = 0xE968EDCD
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData

