from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnPositionParams import SpawnPositionParams as _SpawnPositionParams


class SpawnPositionBlobParams(SubclassBaseFile):
    ResourceType = 0x0B6FBC0D
    ParentResourceType = _SpawnPositionParams.ResourceType
    parent: _SpawnPositionParams
