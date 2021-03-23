from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnStrategyParams import SpawnStrategyParams as _SpawnStrategyParams


class SpawnAbstractAcquisitionParams(SubclassBaseFile):
    ResourceType = 0xB906E397
    ParentResourceType = _SpawnStrategyParams.ResourceType
    parent: _SpawnStrategyParams
