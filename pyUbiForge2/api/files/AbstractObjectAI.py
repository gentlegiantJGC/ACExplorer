from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractEntityAI import AbstractEntityAI as _AbstractEntityAI


class AbstractObjectAI(SubclassBaseFile):
    ResourceType = 0x2CC26564
    ParentResourceType = _AbstractEntityAI.ResourceType
    parent: _AbstractEntityAI

