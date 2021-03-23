from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLObjectCarrier(SubclassBaseFile):
    ResourceType = 0xE424F64B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

