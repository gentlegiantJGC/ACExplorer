from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLTalker(SubclassBaseFile):
    ResourceType = 0xE125F2FE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

