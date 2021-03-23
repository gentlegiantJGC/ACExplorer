from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractCharacterAI import AbstractCharacterAI as _AbstractCharacterAI


class QuadrupedAI(SubclassBaseFile):
    ResourceType = 0xA1E09870
    ParentResourceType = _AbstractCharacterAI.ResourceType
    parent: _AbstractCharacterAI

