from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class RankedMilitaryAnimSetLayer(SubclassBaseFile):
    ResourceType = 0x88842E70
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer

