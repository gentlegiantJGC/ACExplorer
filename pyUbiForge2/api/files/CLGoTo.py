from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLGoTo(SubclassBaseFile):
    ResourceType = 0xE39F6429
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

