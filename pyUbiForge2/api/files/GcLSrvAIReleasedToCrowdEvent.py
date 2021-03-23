from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GcLSrvAIReleasedToCrowdEvent(SubclassBaseFile):
    ResourceType = 0x871C19ED
    ParentResourceType = _Event.ResourceType
    parent: _Event

