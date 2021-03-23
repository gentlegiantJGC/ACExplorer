from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class FollowClip(SubclassBaseFile):
    ResourceType = 0xA6A02794
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip

