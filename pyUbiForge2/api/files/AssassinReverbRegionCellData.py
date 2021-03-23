from pyUbiForge2.api.game import SubclassBaseFile
from .ReverbRegionCellData import ReverbRegionCellData as _ReverbRegionCellData


class AssassinReverbRegionCellData(SubclassBaseFile):
    ResourceType = 0xAE94D868
    ParentResourceType = _ReverbRegionCellData.ResourceType
    parent: _ReverbRegionCellData

