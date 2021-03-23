from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActor import SceneActor as _SceneActor


class MultiEntityActor(SubclassBaseFile):
    ResourceType = 0xEA8C4BA8
    ParentResourceType = _SceneActor.ResourceType
    parent: _SceneActor
