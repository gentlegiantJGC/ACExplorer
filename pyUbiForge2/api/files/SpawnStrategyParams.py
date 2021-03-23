from pyUbiForge2.api.game import SubclassBaseFile
from .SpawningSpecParams import SpawningSpecParams as _SpawningSpecParams


class SpawnStrategyParams(SubclassBaseFile):
    ResourceType = 0x9CC95FE9
    ParentResourceType = _SpawningSpecParams.ResourceType
    parent: _SpawningSpecParams
