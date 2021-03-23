from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainLayer import TerrainLayer as _TerrainLayer


class TerrainCachedHabitatLayer(SubclassBaseFile):
    ResourceType = 0x3093DA11
    ParentResourceType = _TerrainLayer.ResourceType
    parent: _TerrainLayer

