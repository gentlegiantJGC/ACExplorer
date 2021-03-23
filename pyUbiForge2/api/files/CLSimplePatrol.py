from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSimplePatrol(SubclassBaseFile):
    ResourceType = 0x9CCDBEBB
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
