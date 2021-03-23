from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLWagonPassenger(SubclassBaseFile):
    ResourceType = 0xFA7F1428
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

