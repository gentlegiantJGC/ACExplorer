from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnPositionParams import SpawnPositionParams as _SpawnPositionParams


class SpawnPositionStaticParams(SubclassBaseFile):
    ResourceType = 0x3DC5EFD6
    ParentResourceType = _SpawnPositionParams.ResourceType
    parent: _SpawnPositionParams

