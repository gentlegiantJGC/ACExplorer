from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CharacterBeatUpEvent(SubclassBaseFile):
    ResourceType = 0x3FD6D4E1
    ParentResourceType = _Event.ResourceType
    parent: _Event
