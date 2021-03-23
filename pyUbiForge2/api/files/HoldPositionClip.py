from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterLogicClip import CharacterLogicClip as _CharacterLogicClip


class HoldPositionClip(SubclassBaseFile):
    ResourceType = 0x1829BD7E
    ParentResourceType = _CharacterLogicClip.ResourceType
    parent: _CharacterLogicClip

