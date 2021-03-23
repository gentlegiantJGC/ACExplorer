from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractObjectAI import AbstractObjectAI as _AbstractObjectAI


class ObjectAI(SubclassBaseFile):
    ResourceType = 0xED0299F4
    ParentResourceType = _AbstractObjectAI.ResourceType
    parent: _AbstractObjectAI
