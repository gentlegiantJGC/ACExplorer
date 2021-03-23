from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActorSource import SceneActorSource as _SceneActorSource


class SceneActorSourceList(SubclassBaseFile):
    ResourceType = 0x9EBBB35A
    ParentResourceType = _SceneActorSource.ResourceType
    parent: _SceneActorSource

