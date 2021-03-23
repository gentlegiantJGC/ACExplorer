from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class NestedSceneSource(SubclassBaseFile):
    ResourceType = 0x728C446F
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource
