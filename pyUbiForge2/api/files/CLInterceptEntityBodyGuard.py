from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInterceptEntityBodyGuard(SubclassBaseFile):
    ResourceType = 0xA57A69FD
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

