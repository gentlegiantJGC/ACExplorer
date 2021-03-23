from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFightArcher(SubclassBaseFile):
    ResourceType = 0x84BE393A
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

