from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnPositionParams import SpawnPositionParams as _SpawnPositionParams


class SpawnPositionVolumeParams(SubclassBaseFile):
    ResourceType = 0x2DAE7F7A
    ParentResourceType = _SpawnPositionParams.ResourceType
    parent: _SpawnPositionParams
