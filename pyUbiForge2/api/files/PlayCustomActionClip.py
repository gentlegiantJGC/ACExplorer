from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class PlayCustomActionClip(SubclassBaseFile):
    ResourceType = 0x92C9F75A
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip

