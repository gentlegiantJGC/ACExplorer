from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BlockActorResponseEvent(SubclassBaseFile):
    ResourceType = 0xD2F9B32F
    ParentResourceType = _Event.ResourceType
    parent: _Event
