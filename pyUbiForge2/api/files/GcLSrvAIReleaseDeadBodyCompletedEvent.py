from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GcLSrvAIReleaseDeadBodyCompletedEvent(SubclassBaseFile):
    ResourceType = 0x1AEF8104
    ParentResourceType = _Event.ResourceType
    parent: _Event

