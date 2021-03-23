from pyUbiForge2.api.game import SubclassBaseFile
from .SceneEvent import SceneEvent as _SceneEvent


class SceneSkipEvent(SubclassBaseFile):
    ResourceType = 0x536A5F14
    ParentResourceType = _SceneEvent.ResourceType
    parent: _SceneEvent
