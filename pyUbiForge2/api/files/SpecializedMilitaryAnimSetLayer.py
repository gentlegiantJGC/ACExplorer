from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class SpecializedMilitaryAnimSetLayer(SubclassBaseFile):
    ResourceType = 0x444C5C5A
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer
