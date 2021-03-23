from pyUbiForge2.api.game import SubclassBaseFile
from .SceneEvent import SceneEvent as _SceneEvent


class SceneCameraCutEvent(SubclassBaseFile):
    ResourceType = 0xB0B357D4
    ParentResourceType = _SceneEvent.ResourceType
    parent: _SceneEvent

