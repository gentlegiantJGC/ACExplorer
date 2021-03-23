from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainTile import TerrainTile as _TerrainTile


class TerrainHeightTile(SubclassBaseFile):
    ResourceType = 0x772FD699
    ParentResourceType = _TerrainTile.ResourceType
    parent: _TerrainTile

