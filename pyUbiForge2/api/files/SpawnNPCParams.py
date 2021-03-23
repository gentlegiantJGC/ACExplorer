from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnCharacterParams import SpawnCharacterParams as _SpawnCharacterParams


class SpawnNPCParams(SubclassBaseFile):
    ResourceType = 0x94D05600
    ParentResourceType = _SpawnCharacterParams.ResourceType
    parent: _SpawnCharacterParams

