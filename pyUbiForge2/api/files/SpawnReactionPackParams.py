from pyUbiForge2.api.game import SubclassBaseFile
from .SpawningSpecParams import SpawningSpecParams as _SpawningSpecParams


class SpawnReactionPackParams(SubclassBaseFile):
    ResourceType = 0x2A3C8822
    ParentResourceType = _SpawningSpecParams.ResourceType
    parent: _SpawningSpecParams

