from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBlockingGuard(SubclassBaseFile):
    ResourceType = 0x1977CBBD
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

