from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractSceneSpawnerSource import AbstractSceneSpawnerSource as _AbstractSceneSpawnerSource


class SceneSpawningSource(SubclassBaseFile):
    ResourceType = 0x1D625BFD
    ParentResourceType = _AbstractSceneSpawnerSource.ResourceType
    parent: _AbstractSceneSpawnerSource

