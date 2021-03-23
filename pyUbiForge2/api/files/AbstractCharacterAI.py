from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractEntityAI import AbstractEntityAI as _AbstractEntityAI


class AbstractCharacterAI(SubclassBaseFile):
    ResourceType = 0x8F121D69
    ParentResourceType = _AbstractEntityAI.ResourceType
    parent: _AbstractEntityAI
