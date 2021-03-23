from pyUbiForge2.api.game import SubclassBaseFile
from .SpawningSpecParams import SpawningSpecParams as _SpawningSpecParams


class SpawnAutonomousLogicParams(SubclassBaseFile):
    ResourceType = 0x521415E8
    ParentResourceType = _SpawningSpecParams.ResourceType
    parent: _SpawningSpecParams
