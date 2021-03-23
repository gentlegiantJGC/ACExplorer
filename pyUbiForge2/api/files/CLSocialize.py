from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSocialize(SubclassBaseFile):
    ResourceType = 0x0DB60C20
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

