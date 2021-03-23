from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DesynchronizationEvent(SubclassBaseFile):
    ResourceType = 0x84921CD4
    ParentResourceType = _Event.ResourceType
    parent: _Event
