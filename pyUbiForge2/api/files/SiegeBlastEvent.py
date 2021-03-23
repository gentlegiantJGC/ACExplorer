from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SiegeBlastEvent(SubclassBaseFile):
    ResourceType = 0x490E79A2
    ParentResourceType = _Event.ResourceType
    parent: _Event
