from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActor import SceneActor as _SceneActor


class CameraActor(SubclassBaseFile):
    ResourceType = 0xD4E6FA7D
    ParentResourceType = _SceneActor.ResourceType
    parent: _SceneActor

