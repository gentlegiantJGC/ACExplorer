from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnEntityParams import SpawnEntityParams as _SpawnEntityParams


class SpawnObjectParams(SubclassBaseFile):
    ResourceType = 0x6AEB1AE5
    ParentResourceType = _SpawnEntityParams.ResourceType
    parent: _SpawnEntityParams

