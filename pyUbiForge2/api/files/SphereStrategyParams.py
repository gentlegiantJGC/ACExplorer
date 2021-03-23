from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnStrategyParams import SpawnStrategyParams as _SpawnStrategyParams


class SphereStrategyParams(SubclassBaseFile):
    ResourceType = 0x5806157C
    ParentResourceType = _SpawnStrategyParams.ResourceType
    parent: _SpawnStrategyParams

