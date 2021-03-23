from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class SceneReferencingSource(SubclassBaseFile):
    ResourceType = 0x67672A18
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource
