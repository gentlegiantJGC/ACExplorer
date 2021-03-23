from pyUbiForge2.api.game import SubclassBaseFile
from .WangTile import WangTile as _WangTile


class WangTextureTile(SubclassBaseFile):
    ResourceType = 0xB91F3891
    ParentResourceType = _WangTile.ResourceType
    parent: _WangTile

