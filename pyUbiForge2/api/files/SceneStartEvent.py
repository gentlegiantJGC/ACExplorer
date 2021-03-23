from pyUbiForge2.api.game import SubclassBaseFile
from .SceneEvent import SceneEvent as _SceneEvent


class SceneStartEvent(SubclassBaseFile):
    ResourceType = 0x7F9398A3
    ParentResourceType = _SceneEvent.ResourceType
    parent: _SceneEvent
