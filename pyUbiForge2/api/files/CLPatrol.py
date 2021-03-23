from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPatrol(SubclassBaseFile):
    ResourceType = 0xFC0E828E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

