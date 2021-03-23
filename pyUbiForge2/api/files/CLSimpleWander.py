from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSimpleWander(SubclassBaseFile):
    ResourceType = 0xA62733D3
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
