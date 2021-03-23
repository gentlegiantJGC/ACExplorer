from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class AttackClip(SubclassBaseFile):
    ResourceType = 0x76B211E7
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip

