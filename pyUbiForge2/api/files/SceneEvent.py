from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SceneEvent(SubclassBaseFile):
    ResourceType = 0xF3B13D6C
    ParentResourceType = _Event.ResourceType
    parent: _Event
