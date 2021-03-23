from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class AbstractSceneSpawnerSource(SubclassBaseFile):
    ResourceType = 0xF73E56AE
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource

