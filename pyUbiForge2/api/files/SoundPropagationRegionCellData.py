from pyUbiForge2.api.game import SubclassBaseFile
from .RegionCellData import RegionCellData as _RegionCellData


class SoundPropagationRegionCellData(SubclassBaseFile):
    ResourceType = 0xB01FB48A
    ParentResourceType = _RegionCellData.ResourceType
    parent: _RegionCellData

