from pyUbiForge2.api.game import SubclassBaseFile
from .SceneEvent import SceneEvent as _SceneEvent


class SceneOutputEvent(SubclassBaseFile):
    ResourceType = 0x5492F6B2
    ParentResourceType = _SceneEvent.ResourceType
    parent: _SceneEvent

