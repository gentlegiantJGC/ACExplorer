from pyUbiForge2.api.game import SubclassBaseFile
from .SpawningSpecParams import SpawningSpecParams as _SpawningSpecParams


class SpawnPositionParams(SubclassBaseFile):
    ResourceType = 0x05A88480
    ParentResourceType = _SpawningSpecParams.ResourceType
    parent: _SpawningSpecParams
