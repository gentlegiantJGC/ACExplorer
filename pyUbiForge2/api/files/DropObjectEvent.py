from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DropObjectEvent(SubclassBaseFile):
    ResourceType = 0x46D8B31E
    ParentResourceType = _Event.ResourceType
    parent: _Event
