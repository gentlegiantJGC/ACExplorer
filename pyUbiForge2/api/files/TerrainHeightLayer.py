from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainLayer import TerrainLayer as _TerrainLayer


class TerrainHeightLayer(SubclassBaseFile):
    ResourceType = 0x6A646E9C
    ParentResourceType = _TerrainLayer.ResourceType
    parent: _TerrainLayer

