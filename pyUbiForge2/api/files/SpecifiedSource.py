from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class SpecifiedSource(SubclassBaseFile):
    ResourceType = 0xE7FE1FE6
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource

