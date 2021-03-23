from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSurrender(SubclassBaseFile):
    ResourceType = 0x51AD32A0
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
