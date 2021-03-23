from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInterceptEntityDefault(SubclassBaseFile):
    ResourceType = 0x2F95E859
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

