from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterActor import CharacterActor as _CharacterActor


class NPCActor(SubclassBaseFile):
    ResourceType = 0xB0BA1023
    ParentResourceType = _CharacterActor.ResourceType
    parent: _CharacterActor
