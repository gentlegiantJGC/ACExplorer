from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLNPCDeath(SubclassBaseFile):
    ResourceType = 0xD80B685B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

