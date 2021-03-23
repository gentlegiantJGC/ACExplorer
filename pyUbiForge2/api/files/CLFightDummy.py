from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFightDummy(SubclassBaseFile):
    ResourceType = 0x39CDA68E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

