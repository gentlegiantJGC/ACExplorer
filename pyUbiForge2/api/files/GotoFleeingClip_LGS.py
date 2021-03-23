from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class GotoFleeingClip_LGS(SubclassBaseFile):
    ResourceType = 0xC7B59DE6
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip
