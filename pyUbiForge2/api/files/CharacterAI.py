from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractCharacterAI import AbstractCharacterAI as _AbstractCharacterAI


class CharacterAI(SubclassBaseFile):
    ResourceType = 0x516CC959
    ParentResourceType = _AbstractCharacterAI.ResourceType
    parent: _AbstractCharacterAI
