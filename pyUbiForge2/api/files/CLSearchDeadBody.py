from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSearchDeadBody(SubclassBaseFile):
    ResourceType = 0x65FAD2E2
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

