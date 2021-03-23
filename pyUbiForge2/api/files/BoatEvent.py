from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BoatEvent(SubclassBaseFile):
    ResourceType = 0x9E995700
    ParentResourceType = _Event.ResourceType
    parent: _Event
