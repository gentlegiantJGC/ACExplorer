from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnEntityParams import SpawnEntityParams as _SpawnEntityParams


class SpawnCharacterParams(SubclassBaseFile):
    ResourceType = 0xFB7FF6A5
    ParentResourceType = _SpawnEntityParams.ResourceType
    parent: _SpawnEntityParams
