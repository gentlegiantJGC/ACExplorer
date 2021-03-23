from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CharacterPoisonEvent(SubclassBaseFile):
    ResourceType = 0x5ABC0BD4
    ParentResourceType = _Event.ResourceType
    parent: _Event
