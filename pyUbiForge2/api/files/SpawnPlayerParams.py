from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnCharacterParams import SpawnCharacterParams as _SpawnCharacterParams


class SpawnPlayerParams(SubclassBaseFile):
    ResourceType = 0x51BA3541
    ParentResourceType = _SpawnCharacterParams.ResourceType
    parent: _SpawnCharacterParams
