from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLWait(SubclassBaseFile):
    ResourceType = 0x59959FEE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

