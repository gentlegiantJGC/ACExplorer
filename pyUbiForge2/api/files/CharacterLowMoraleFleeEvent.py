from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterFleeEvent import CharacterFleeEvent as _CharacterFleeEvent


class CharacterLowMoraleFleeEvent(SubclassBaseFile):
    ResourceType = 0x5ED51062
    ParentResourceType = _CharacterFleeEvent.ResourceType
    parent: _CharacterFleeEvent
