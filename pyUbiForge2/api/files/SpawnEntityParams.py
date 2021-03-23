from pyUbiForge2.api.game import SubclassBaseFile
from .SpawningSpecParams import SpawningSpecParams as _SpawningSpecParams


class SpawnEntityParams(SubclassBaseFile):
    ResourceType = 0x423C7BFE
    ParentResourceType = _SpawningSpecParams.ResourceType
    parent: _SpawningSpecParams
