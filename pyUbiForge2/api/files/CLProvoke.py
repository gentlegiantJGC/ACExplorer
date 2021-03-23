from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLProvoke(SubclassBaseFile):
    ResourceType = 0xB7770DC9
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
