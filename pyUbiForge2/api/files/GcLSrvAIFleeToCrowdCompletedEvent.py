from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GcLSrvAIFleeToCrowdCompletedEvent(SubclassBaseFile):
    ResourceType = 0xA760455F
    ParentResourceType = _Event.ResourceType
    parent: _Event
