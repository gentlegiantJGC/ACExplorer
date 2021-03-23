from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnObjectParams import SpawnObjectParams as _SpawnObjectParams


class SpawnInventoryParams(SubclassBaseFile):
    ResourceType = 0xD920BAC7
    ParentResourceType = _SpawnObjectParams.ResourceType
    parent: _SpawnObjectParams

