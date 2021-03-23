from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainTile import TerrainTile as _TerrainTile


class TerrainCachedHabitatTile(SubclassBaseFile):
    ResourceType = 0x85444067
    ParentResourceType = _TerrainTile.ResourceType
    parent: _TerrainTile
