from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ActivateEvent(SubclassBaseFile):
    ResourceType = 0xB0011C8A
    ParentResourceType = _Event.ResourceType
    parent: _Event

