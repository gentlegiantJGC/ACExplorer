from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBodyGuard(SubclassBaseFile):
    ResourceType = 0xA2214F90
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

