from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterActor import CharacterActor as _CharacterActor


class PlayerActor(SubclassBaseFile):
    ResourceType = 0xFC17D602
    ParentResourceType = _CharacterActor.ResourceType
    parent: _CharacterActor

