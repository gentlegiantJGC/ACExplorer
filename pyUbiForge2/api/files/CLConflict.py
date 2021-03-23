from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLConflict(SubclassBaseFile):
    ResourceType = 0x7F8F0456
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

