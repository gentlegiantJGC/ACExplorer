from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHarass(SubclassBaseFile):
    ResourceType = 0x43FF1025
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
