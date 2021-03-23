from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLAbstractReaction(SubclassBaseFile):
    ResourceType = 0x8F94BD8E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

