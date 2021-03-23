from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class FromCrowdSource(SubclassBaseFile):
    ResourceType = 0xA5E9F6AA
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource

