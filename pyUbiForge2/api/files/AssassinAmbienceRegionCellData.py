from pyUbiForge2.api.game import SubclassBaseFile
from .AmbienceRegionCellData import AmbienceRegionCellData as _AmbienceRegionCellData


class AssassinAmbienceRegionCellData(SubclassBaseFile):
    ResourceType = 0xF02FBD93
    ParentResourceType = _AmbienceRegionCellData.ResourceType
    parent: _AmbienceRegionCellData
