from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class GotoClip(SubclassBaseFile):
    ResourceType = 0x9C03E39F
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip
