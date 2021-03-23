from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class ParentEntitySource(SubclassBaseFile):
    ResourceType = 0x0E0C6066
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource
