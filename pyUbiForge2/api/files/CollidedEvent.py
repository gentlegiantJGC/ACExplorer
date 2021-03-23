from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CollidedEvent(SubclassBaseFile):
    ResourceType = 0x7DE48E7E
    ParentResourceType = _Event.ResourceType
    parent: _Event
