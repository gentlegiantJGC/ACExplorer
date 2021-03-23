from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NPCArmedStatusChangedEvent(SubclassBaseFile):
    ResourceType = 0x3A6D529B
    ParentResourceType = _Event.ResourceType
    parent: _Event

