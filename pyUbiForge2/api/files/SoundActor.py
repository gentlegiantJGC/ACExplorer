from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActor import SceneActor as _SceneActor


class SoundActor(SubclassBaseFile):
    ResourceType = 0xDDB970A8
    ParentResourceType = _SceneActor.ResourceType
    parent: _SceneActor
