from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLWander(SubclassBaseFile):
    ResourceType = 0xC6E40FE6
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
