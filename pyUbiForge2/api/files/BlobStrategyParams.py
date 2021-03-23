from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnStrategyParams import SpawnStrategyParams as _SpawnStrategyParams


class BlobStrategyParams(SubclassBaseFile):
    ResourceType = 0x68882CCC
    ParentResourceType = _SpawnStrategyParams.ResourceType
    parent: _SpawnStrategyParams

