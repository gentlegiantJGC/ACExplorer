from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSearchArcher(SubclassBaseFile):
    ResourceType = 0x29BF371D
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

