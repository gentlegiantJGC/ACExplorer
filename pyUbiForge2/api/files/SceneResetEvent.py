from pyUbiForge2.api.game import SubclassBaseFile
from .SceneEvent import SceneEvent as _SceneEvent


class SceneResetEvent(SubclassBaseFile):
    ResourceType = 0xB70D31B9
    ParentResourceType = _SceneEvent.ResourceType
    parent: _SceneEvent
