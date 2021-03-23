from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainLayer import TerrainLayer as _TerrainLayer


class TerrainHabitatLayer(SubclassBaseFile):
    ResourceType = 0x5FB94FF1
    ParentResourceType = _TerrainLayer.ResourceType
    parent: _TerrainLayer
