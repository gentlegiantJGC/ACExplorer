from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLGuardPost(SubclassBaseFile):
    ResourceType = 0x228DFEAF
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

