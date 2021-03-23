from pyUbiForge2.api.game import SubclassBaseFile
from .TerrainTile import TerrainTile as _TerrainTile


class TerrainHabitatTile(SubclassBaseFile):
    ResourceType = 0x1FA641B1
    ParentResourceType = _TerrainTile.ResourceType
    parent: _TerrainTile

