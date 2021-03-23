from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSimpleGoTo(SubclassBaseFile):
    ResourceType = 0x8D6978AE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

